"""The opponent group must be supplied explicitly for every remote series."""

import secrets
from types import SimpleNamespace

import pytest

from salareen_cop.official.series import SAFE_ID, OfficialSeries
from salareen_cop.official.terms import (
    GROUP_ID,
    TERMS,
    commit_of,
    derive_game_ids,
)

GROUPS = ["GRP00001", "amireman", "zeta.group-9", "a"]


def _turn(sender: str) -> dict:
    return {
        "step": 1,
        "sender": sender,
        "commit": "b" * 64,
        "hint": "",
        "smell_grid": {},
        "timestamp": "",
        "barrier_placed": None,
        "capture_claim": None,
        "claim_response": None,
        "win_claim": None,
    }


def _peer_greeting(group: str, role: str, number: int) -> dict:
    nonce = secrets.token_hex(16)
    return {
        "terms": dict(TERMS),
        "nonce": nonce,
        "signature": commit_of(TERMS, nonce),
        "group_id": group,
        "role": role,
        "sub_game_number": number,
        "identity": {"group_id": group, "github_commit": "9" * 40},
        "game_uid": derive_game_ids(GROUP_ID, group)[1],
    }


class StubEngine:
    def __init__(self, role: str) -> None:
        self.role = role
        self.step = 1
        self.records: list[dict] = []

    def receive(self, message: dict) -> SimpleNamespace:
        return SimpleNamespace(won=True, caught=False, opponent_won=False)

    def take_turn(self, incoming=None, *, hold: bool = False) -> dict:
        return _turn(self.role)


class StubTransport:
    """Answers one greeting and one turn per sub-game, then goes quiet."""

    def __init__(self, group: str) -> None:
        self.group = group
        self.audits: list[dict] = []
        self._turn: dict | None = None

    def exchange_agreement(self, offer: dict, timeout: float = 300.0) -> dict:
        peer_role = "thief" if offer["role"] == "police" else "police"
        self._turn = _turn(peer_role)
        return _peer_greeting(self.group, peer_role, offer["sub_game_number"])

    def send_turn(self, message: dict) -> None:
        return None

    def poll_turn(self, timeout: float) -> dict | None:
        turn, self._turn = self._turn, None
        return turn

    def send_audit(self, payload: dict) -> None:
        self.audits.append(payload)

    def poll_audit(self, timeout: float) -> dict | None:
        return None

    def send_control(self, message: dict) -> None:
        return None


def _series(group: str, game_id: str | None = None) -> OfficialSeries:
    return OfficialSeries(
        StubTransport(group),
        SimpleNamespace(set_offer=lambda offer: None),
        lambda role, number, commit: StubEngine(role),
        {"police": "1" * 40, "thief": "2" * 40},
        opponent_group=group,
        game_id=game_id,
    )


@pytest.mark.parametrize("group", GROUPS)
def test_any_opponent_group_completes_a_six_game_series(group):
    result = _series(group, f"NC-{group}").run(turn_timeout=0.01)
    assert len(result.summaries) == 6
    assert result.game_id == f"NC-{group}"
    assert result.game_uid == derive_game_ids(GROUP_ID, group)[1]
    assert result.peer_identity["group_id"] == group


@pytest.mark.parametrize("group", GROUPS)
def test_derived_ids_are_unique_per_opponent_group(group):
    game_id, game_uid = derive_game_ids(GROUP_ID, group)
    assert game_id == "-vs-".join(sorted([GROUP_ID, group]))
    others = {derive_game_ids(GROUP_ID, other)[1] for other in GROUPS if other != group}
    assert game_uid not in others


def test_series_no_longer_defaults_to_any_opponent():
    assert OfficialSeries(None, None, None, {}).opponent is None


@pytest.mark.parametrize("bad", [None, "", "has space", "semi;colon", GROUP_ID])
def test_run_rejects_a_missing_or_unsafe_opponent_group(bad):
    series = _series("GRP00001")
    series.opponent = bad
    with pytest.raises(ValueError):
        series.run(turn_timeout=0.01)


def test_run_rejects_an_unsafe_game_id():
    with pytest.raises(ValueError, match="game_id"):
        _series("GRP00001", "bad id/../x").run(turn_timeout=0.01)


def test_peer_group_mismatch_is_still_rejected():
    series = _series("GRP00001")
    series.transport = StubTransport("someone-else")
    with pytest.raises(ValueError, match="opponent group changed"):
        series.run(turn_timeout=0.01)


def test_safe_id_pattern_accepts_and_rejects():
    assert all(SAFE_ID.fullmatch(group) for group in GROUPS)
    assert not any(SAFE_ID.fullmatch(bad) for bad in ["", "a b", "a/b", "a:b"])
