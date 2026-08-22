"""A turn delivered early for the next subgame must survive the handoff."""

import queue
import secrets
from types import SimpleNamespace

from salareen_cop.official.runtime import SubGameRuntime
from salareen_cop.official.series import OfficialSeries
from salareen_cop.official.terms import GROUP_ID, TERMS, commit_of, derive_game_ids

GROUP = "GRP00001"


def turn(sender: str, step: int = 1, digest: str | None = None) -> dict:
    return {
        "step": step,
        "sender": sender,
        "commit": digest or ("b" * 64),
        "hint": "",
        "smell_grid": {},
        "timestamp": "",
        "barrier_placed": None,
        "capture_claim": None,
        "claim_response": None,
        "win_claim": None,
    }


def peer_role(number: int) -> str:
    return "thief" if number % 2 else "police"


class StubEngine:
    def __init__(self, role: str) -> None:
        self.role = role
        self.step = 1
        self.records: list[dict] = []
        self.received: list[dict] = []

    def receive(self, message: dict) -> SimpleNamespace:
        self.received.append(message)
        return SimpleNamespace(won=True, caught=False, opponent_won=False)

    def take_turn(self, incoming=None, *, hold: bool = False) -> dict:
        return turn(self.role)


class PipeliningTransport:
    """Opponent that pushes the next Thief move during the prior audit window."""

    def __init__(self) -> None:
        self.turns: queue.Queue = queue.Queue()
        self.audits: queue.Queue = queue.Queue()
        self.current = 0
        self.replied: set[int] = set()
        self.sent_audits: list[dict] = []

    def exchange_agreement(self, offer: dict, timeout: float = 300.0) -> dict:
        self.current = offer["sub_game_number"]
        role = peer_role(self.current)
        if self.current == 1 and role == "thief":
            self.turns.put(turn("thief"))
        nonce = secrets.token_hex(16)
        return {
            "terms": dict(TERMS),
            "nonce": nonce,
            "signature": commit_of(TERMS, nonce),
            "group_id": GROUP,
            "role": role,
            "sub_game_number": self.current,
            "identity": {"group_id": GROUP, "github_commit": "9" * 40},
            "game_uid": derive_game_ids(GROUP_ID, GROUP)[1],
        }

    def send_turn(self, message: dict) -> None:
        if peer_role(self.current) == "police" and self.current not in self.replied:
            self.replied.add(self.current)
            self.turns.put(turn("police"))

    def poll_turn(self, timeout: float) -> dict | None:
        try:
            return self.turns.get(timeout=max(timeout, 0.0))
        except queue.Empty:
            return None

    def send_audit(self, payload: dict) -> None:
        self.sent_audits.append(payload)
        if payload.get("result_claim") == "series_consensus":
            return
        number = payload["sub_game_number"]
        self.audits.put(
            {
                "sender": peer_role(number),
                "records": [],
                "result_claim": payload["result_claim"],
                "sub_game": number,
                "sub_game_number": number,
            }
        )
        following = number + 1
        if following <= 6 and peer_role(following) == "thief":
            self.turns.put(turn("thief"))

    def poll_audit(self, timeout: float) -> dict | None:
        try:
            return self.audits.get(timeout=max(timeout, 0.0))
        except queue.Empty:
            return None

    def send_control(self, message: dict) -> None:
        return None


def test_audit_window_does_not_discard_the_next_subgame_turn():
    transport = PipeliningTransport()
    runtime = SubGameRuntime(StubEngine("thief"), transport, 2)
    runtime.result = "capture"
    runtime._finish(0.05)
    assert transport.turns.qsize() == 1, "the pipelined SG3 turn was drained"


def test_next_subgame_consumes_the_early_turn():
    transport = PipeliningTransport()
    finished = SubGameRuntime(StubEngine("thief"), transport, 2)
    finished.result = "capture"
    finished._finish(0.05)
    police = StubEngine("police")
    summary = SubGameRuntime(police, transport, 3).run(turn_timeout=0.4)
    assert summary["result"] != "timeout"
    assert len(police.received) == 1


def test_six_subgames_complete_with_a_pipelining_opponent():
    transport = PipeliningTransport()
    series = OfficialSeries(
        transport,
        SimpleNamespace(set_offer=lambda offer: None),
        lambda role, number, commit: StubEngine(role),
        {"police": "1" * 40, "thief": "2" * 40},
        opponent_group=GROUP,
        game_id="GRP00001-vs-salareen",
    )
    result = series.run(turn_timeout=0.4)
    assert len(result.summaries) == 6
    assert [s["result"] for s in result.summaries] == ["capture"] * 6
    assert all(s["audit"]["result_agreed"] for s in result.summaries)
