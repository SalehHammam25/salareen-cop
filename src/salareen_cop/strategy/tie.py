"""Stable cop pursuit and barrier ordering."""

from salareen_cop.base_logic.actions import MoveChoice

MOVEMENT_ORDER = (
    MoveChoice.NORTH,
    MoveChoice.SOUTH,
    MoveChoice.EAST,
    MoveChoice.WEST,
)


def configured_order_tie(choices: tuple[MoveChoice, ...]) -> MoveChoice:
    return next(choice for choice in MOVEMENT_ORDER if choice in choices)
