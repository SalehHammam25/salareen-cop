"""Cop pursuit path and result tests."""

import pytest

from salareen_cop.base_logic.state_factory import build_state
from salareen_cop.base_logic.state_results import StateAccepted
from salareen_cop.base_logic.state_types import Board, Coordinate, EpisodeStatus
from salareen_cop.strategy.blind import BlindCopPolicy
from salareen_cop.strategy.gateway import StrategyGateway
from salareen_cop.strategy.models import StrategySnapshot, snapshot_for
from salareen_cop.strategy.results import (
    DecisionError,
    DecisionFailure,
    ProposedAction,
    ValidatedDecision,
)


def state_with(config, *, cop, thief=None, barriers=()):
    thief = Coordinate(6, 6) if thief is None else thief
    result = build_state(
        config,
        thief=thief,
        cop=cop,
        barriers=barriers,
        barrier_usage=len(tuple(barriers)),
    )
    assert isinstance(result, StateAccepted)
    return result.value


def test_open_board_pursuit_reduces_shortest_distance(rules, initial_game) -> None:
    result = StrategyGateway(rules, BlindCopPolicy()).decide(
        initial_game, Coordinate(2, 2)
    )
    assert isinstance(result, ValidatedDecision)
    assert result.state.positions.cop == Coordinate(1, 0)
    assert initial_game.positions.cop == Coordinate(0, 0)


def test_barrier_aware_shortest_path(accepted_config, rules) -> None:
    state = state_with(
        accepted_config,
        cop=Coordinate(3, 3),
        barriers=(Coordinate(2, 3), Coordinate(3, 4)),
    )
    result = StrategyGateway(rules, BlindCopPolicy()).decide(state, Coordinate(2, 4))
    assert isinstance(result, ValidatedDecision)
    assert result.state.positions.cop == Coordinate(4, 3)


@pytest.mark.parametrize(
    ("target", "expected"),
    [
        (Coordinate(2, 2), "N"),
        (Coordinate(2, 4), "N"),
        (Coordinate(4, 2), "S"),
        (Coordinate(4, 4), "S"),
    ],
)
def test_all_symmetric_ties_are_stable(accepted_config, target, expected) -> None:
    state = state_with(accepted_config, cop=Coordinate(3, 3))
    result = BlindCopPolicy().propose(snapshot_for(state, target))
    assert isinstance(result, ProposedAction)
    assert result.action.choice == expected


def test_target_reached_uses_stay(rules, initial_game) -> None:
    result = StrategyGateway(rules, BlindCopPolicy()).decide(
        initial_game, initial_game.positions.cop
    )
    assert isinstance(result, ValidatedDecision)
    assert result.action.choice == "STAY"


def test_unreachable_and_invalid_targets_are_explicit(accepted_config) -> None:
    barriers = (Coordinate(2, 3), Coordinate(3, 2), Coordinate(3, 4), Coordinate(4, 3))
    state = state_with(accepted_config, cop=Coordinate(0, 0), barriers=barriers)
    result = BlindCopPolicy().propose(snapshot_for(state, Coordinate(3, 3)))
    assert result == DecisionFailure(DecisionError.UNREACHABLE_TARGET)
    invalid = BlindCopPolicy().propose(snapshot_for(state, Coordinate(-1, 0)))
    assert invalid == DecisionFailure(DecisionError.INVALID_TARGET)


def test_terminal_state_is_explicit(rules, initial_game) -> None:
    terminal = rules.technical_loss(initial_game).state
    result = BlindCopPolicy().propose(snapshot_for(terminal, Coordinate(2, 2)))
    assert result == DecisionFailure(DecisionError.TERMINAL_STATE)


@pytest.mark.parametrize("size", [8, 50, 100])
def test_large_boards_obey_n_squared_bound(size) -> None:
    snapshot = StrategySnapshot(
        Board(size, 0, "top-left"),
        Coordinate(0, 0),
        frozenset(),
        14,
        EpisodeStatus.ACTIVE,
        Coordinate(size - 1, size - 1),
    )
    result = BlindCopPolicy().propose(snapshot)
    assert isinstance(result, ProposedAction)
    assert result.explored_cells <= size**2
