"""Base Logic validation and malicious proposal tests."""

from salareen_cop.base_logic.actions import BarrierAction, MoveAction, MoveChoice
from salareen_cop.base_logic.state_types import Coordinate, Role
from salareen_cop.strategy.gateway import StrategyGateway
from salareen_cop.strategy.results import (
    DecisionError,
    DecisionFailure,
    ProposedAction,
)


class WrongRole:
    def propose(self, snapshot):
        return ProposedAction(MoveAction(Role.THIEF, MoveChoice.STAY), 0)


class Diagonal:
    def propose(self, snapshot):
        return ProposedAction(
            MoveAction(Role.COP, MoveChoice.SOUTH, Coordinate(1, 1)), 0
        )


class IllegalBarrier:
    def propose(self, snapshot):
        return ProposedAction(BarrierAction(Role.COP, Coordinate(6, 6)), 0)


class Exploding:
    def propose(self, snapshot):
        raise RuntimeError("private-coordinate-and-token")


def test_wrong_role_rejected_without_mutation(rules, initial_game) -> None:
    result = StrategyGateway(rules, WrongRole()).decide(initial_game, Coordinate(2, 2))
    assert result == DecisionFailure(DecisionError.ILLEGAL_PROPOSAL)
    assert initial_game.positions.cop == Coordinate(0, 0)


def test_move_and_barrier_cannot_bypass_base_logic(rules, initial_game) -> None:
    for policy in (Diagonal(), IllegalBarrier()):
        result = StrategyGateway(rules, policy).decide(initial_game, Coordinate(2, 2))
        assert result == DecisionFailure(DecisionError.ILLEGAL_PROPOSAL)
        assert initial_game.positions.cop == Coordinate(0, 0)


def test_runtime_message_is_sanitized(rules, initial_game) -> None:
    result = StrategyGateway(rules, Exploding()).decide(initial_game, Coordinate(2, 2))
    assert result == DecisionFailure(DecisionError.POLICY_EXCEPTION, "RuntimeError")
    assert "private-coordinate" not in str(result)
