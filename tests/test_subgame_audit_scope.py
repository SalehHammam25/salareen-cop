"""Inbound audits must be scoped to the subgame that is actually running."""

import queue

import pytest

from salareen_cop.official.audit_window import await_window, matches, sweep_backlog
from salareen_cop.official.runtime import SubGameRuntime


class AuditTransport:
    """Only the audit queue matters here; it behaves like the real mailbox."""

    def __init__(self, reply: dict | None = None) -> None:
        self.audits: queue.Queue = queue.Queue()
        self.turns: queue.Queue = queue.Queue()
        self.sent_audits: list[dict] = []
        self.reply = reply

    def send_audit(self, payload: dict) -> None:
        """Announce our audit; the peer answers inside the window."""
        self.sent_audits.append(payload)
        if self.reply is not None:
            self.audits.put(self.reply)

    def poll_audit(self, timeout: float) -> dict | None:
        try:
            return self.audits.get(timeout=max(timeout, 0.0))
        except queue.Empty:
            return None

    def poll_turn(self, timeout: float) -> dict | None:
        try:
            return self.turns.get(timeout=max(timeout, 0.0))
        except queue.Empty:
            return None

    def send_turn(self, message: dict) -> None:
        return None


class StubEngine:
    def __init__(self, role: str = "police") -> None:
        self.role = role
        self.step = 1
        self.records: list[dict] = []


def audit(claim: str = "capture", **tags) -> dict:
    return {"sender": "thief", "records": [], "result_claim": claim, **tags}


def _runtime(transport, sub_game: int, result: str = "capture") -> SubGameRuntime:
    runtime = SubGameRuntime(StubEngine(), transport, sub_game)
    runtime.result = result
    return runtime


def test_outbound_audit_carries_both_matching_tags():
    transport = AuditTransport()
    _runtime(transport, 4)._finish(0.01)
    envelope = transport.sent_audits[0]
    assert envelope["sub_game"] == 4
    assert envelope["sub_game_number"] == 4
    assert envelope["sub_game"] == envelope["sub_game_number"]


@pytest.mark.parametrize("sub_game", [1, 2, 3, 4, 5, 6])
def test_every_subgame_tags_its_own_number(sub_game):
    transport = AuditTransport()
    _runtime(transport, sub_game)._finish(0.01)
    envelope = transport.sent_audits[0]
    assert envelope["sub_game"] == sub_game
    assert envelope["sub_game_number"] == sub_game


def test_tagged_audit_for_this_subgame_is_accepted():
    transport = AuditTransport()
    transport.audits.put(audit(sub_game=3, sub_game_number=3))
    summary = _runtime(transport, 3)._finish(0.05)
    assert summary["audit"]["peer_result_claim"] == "capture"
    assert summary["audit"]["result_agreed"] is True


def test_tagged_audit_from_another_subgame_is_ignored():
    transport = AuditTransport()
    transport.audits.put(audit(sub_game=3, sub_game_number=3))
    summary = _runtime(transport, 4)._finish(0.05)
    assert summary["audit"]["peer_result_claim"] is None
    assert summary["result"] == "capture"


def test_audit_with_contradictory_tags_is_ignored():
    transport = AuditTransport()
    transport.audits.put(audit(sub_game=5, sub_game_number=6))
    summary = _runtime(transport, 5)._finish(0.05)
    assert summary["audit"]["peer_result_claim"] is None
    summary = _runtime(transport, 6)._finish(0.05)
    assert summary["audit"]["peer_result_claim"] is None


def test_untagged_audit_arriving_in_the_window_stays_compatible():
    transport = AuditTransport(reply=audit())
    summary = _runtime(transport, 2)._finish(0.05)
    assert summary["audit"]["peer_result_claim"] == "capture"
    assert summary["audit"]["result_agreed"] is True


def test_untagged_stale_audit_cannot_terminate_a_later_subgame():
    transport = AuditTransport()
    transport.audits.put(audit(claim="timeout"))
    summary = _runtime(transport, 4)._finish(0.05)
    assert summary["audit"]["peer_result_claim"] is None
    assert summary["audit"]["result_agreed"] is False
    assert summary["result"] == "capture"


def test_series_consensus_envelope_is_never_taken_as_a_subgame_audit():
    transport = AuditTransport()
    transport.audits.put(
        {
            "sender": "thief",
            "records": [],
            "result_claim": "series_consensus",
            "consensus_sha": "a" * 64,
        }
    )
    assert sweep_backlog(transport, 1) is None


def test_matches_rules():
    assert matches({}, 3, allow_untagged=True) is True
    assert matches({}, 3, allow_untagged=False) is False
    assert matches({"sub_game": 3}, 3, allow_untagged=False) is True
    assert matches({"sub_game": 2}, 3, allow_untagged=True) is False
    assert matches({"sub_game": 3, "sub_game_number": 4}, 3, allow_untagged=True) is False


def test_await_window_returns_none_when_nothing_arrives():
    assert await_window(AuditTransport(), 1, 0.02) is None


def test_tagged_reply_inside_the_window_is_accepted():
    transport = AuditTransport(reply=audit(sub_game=6, sub_game_number=6))
    summary = _runtime(transport, 6)._finish(0.05)
    assert summary["audit"]["result_agreed"] is True
