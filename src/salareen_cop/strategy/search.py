"""Bounded breadth-first search over permitted geometry."""

from collections import deque

from salareen_cop.base_logic.actions import MoveChoice
from salareen_cop.base_logic.movement import target_for, validate_target
from salareen_cop.base_logic.state_types import Coordinate

from .models import StrategySnapshot
from .tie import MOVEMENT_ORDER


def distance_map(
    snapshot: StrategySnapshot,
    extra_barrier: Coordinate | None = None,
) -> dict[Coordinate, int]:
    blocked = snapshot.barriers | ({extra_barrier} if extra_barrier else set())
    if not snapshot.board.contains(snapshot.target) or snapshot.target in blocked:
        return {}
    distances = {snapshot.target: 0}
    pending = deque([snapshot.target])
    while pending and len(distances) <= snapshot.board.grid_size**2:
        current = pending.popleft()
        for choice in MOVEMENT_ORDER:
            neighbor = target_for(current, choice)
            if (
                snapshot.board.contains(neighbor)
                and neighbor not in blocked
                and neighbor not in distances
            ):
                distances[neighbor] = distances[current] + 1
                pending.append(neighbor)
    return distances


def shortest_choices(
    snapshot: StrategySnapshot, distances: dict[Coordinate, int]
) -> tuple[MoveChoice, ...]:
    candidates = []
    for choice in MOVEMENT_ORDER:
        target = target_for(snapshot.cop, choice)
        if (
            validate_target(
                snapshot.board, snapshot.cop, target, snapshot.barriers
            )
            is None
            and target in distances
        ):
            candidates.append((choice, distances[target]))
    if not candidates:
        return ()
    best = min(distance for _, distance in candidates)
    return tuple(choice for choice, distance in candidates if distance == best)
