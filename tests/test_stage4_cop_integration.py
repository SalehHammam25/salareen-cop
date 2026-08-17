"""Cop belief target and Stage 3 integration tests."""

from decimal import Decimal

from salareen_cop.base_logic.state_types import Coordinate
from salareen_cop.belief.integration import BeliefStrategyAdapter
from salareen_cop.belief.models import BeliefMap
from salareen_cop.belief.prior import uniform_prior
from salareen_cop.belief.target import select_target
from salareen_cop.strategy.blind import BlindCopPolicy
from salareen_cop.strategy.gateway import StrategyGateway
from salareen_cop.strategy.results import ValidatedDecision


def test_uniform_belief_target_is_repeatable(initial_game) -> None:
    belief = uniform_prior(initial_game.board, initial_game.barriers)
    assert select_target(belief) == select_target(belief)


def test_exact_maximum_tie_is_row_major(initial_game) -> None:
    zero, half = Decimal("0"), Decimal("0.5")
    rows = [[zero] * 7 for _ in range(7)]
    rows[1][1] = half
    rows[2][2] = half
    belief = BeliefMap(initial_game.board, tuple(tuple(row) for row in rows))
    assert select_target(belief) == Coordinate(1, 1)


def test_highest_thief_belief_becomes_restricted_target(
    rules, initial_game
) -> None:
    zero = Decimal("0")
    rows = [[zero] * 7 for _ in range(7)]
    rows[2][2] = Decimal("1")
    belief = BeliefMap(initial_game.board, tuple(tuple(row) for row in rows))
    adapter = BeliefStrategyAdapter(StrategyGateway(rules, BlindCopPolicy()))
    result = adapter.decide(initial_game, belief)
    assert isinstance(result, ValidatedDecision)
    assert result.state.positions.cop == Coordinate(1, 0)
    assert initial_game.positions.cop == Coordinate(0, 0)


def test_belief_contains_no_action_or_game_state(initial_game) -> None:
    belief = uniform_prior(initial_game.board, initial_game.barriers)
    assert not hasattr(belief, "action")
    assert not hasattr(belief, "state")
    assert not hasattr(belief, "thief")
