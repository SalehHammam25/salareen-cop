"""Immutable restricted inputs for blind cop strategy."""

from dataclasses import dataclass

from salareen_cop.base_logic.state_types import (
    Board,
    Coordinate,
    EpisodeStatus,
    GameState,
)


@dataclass(frozen=True, slots=True)
class StrategySnapshot:
    board: Board
    cop: Coordinate
    barriers: frozenset[Coordinate]
    remaining_barriers: int
    status: EpisodeStatus
    target: Coordinate


def snapshot_for(state: GameState, target: Coordinate) -> StrategySnapshot:
    """Expose own geometry and an injected target, never thief truth."""
    return StrategySnapshot(
        state.board,
        state.positions.cop,
        state.barriers,
        state.barrier_quota - state.barrier_usage,
        state.status,
        target,
    )
