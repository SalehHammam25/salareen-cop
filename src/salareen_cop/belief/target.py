"""Deterministic belief-to-pursuit-target boundary."""

from salareen_cop.base_logic.state_types import Coordinate

from .models import BeliefMap


def select_target(belief: BeliefMap) -> Coordinate:
    """Choose maximum probability in stable row-major order."""
    start = belief.board.axis_start_index
    candidates = (
        (belief.probabilities[row][col], Coordinate(start + row, start + col))
        for row in range(belief.board.grid_size)
        for col in range(belief.board.grid_size)
    )
    return max(candidates, key=lambda item: (item[0], -item[1].row, -item[1].col))[1]
