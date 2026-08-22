"""Duplicate absorption and equivocation detection survive the audit fix."""

import pytest

from salareen_cop.official.delivery import EquivocationError
from salareen_cop.official.runtime import SubGameRuntime


def turn(step: int = 1, digest: str = "b" * 64) -> dict:
    return {"step": step, "sender": "thief", "commit": digest}


class StubEngine:
    role = "police"
    step = 1
    records: list[dict] = []


def _runtime() -> SubGameRuntime:
    return SubGameRuntime(StubEngine(), None, 3)


def test_same_step_same_commit_is_absorbed():
    runtime = _runtime()
    assert runtime.delivery.offer(turn()) != []
    assert runtime.delivery.offer(turn()) == []
    assert runtime.delivery.offer(turn()) == []


def test_same_step_different_commit_is_equivocation():
    runtime = _runtime()
    runtime.delivery.offer(turn(1, "b" * 64))
    with pytest.raises(EquivocationError):
        runtime.delivery.offer(turn(1, "c" * 64))


def test_each_subgame_starts_with_a_fresh_inbox():
    first, second = _runtime(), _runtime()
    first.delivery.offer(turn())
    assert first.delivery.played and not second.delivery.played
