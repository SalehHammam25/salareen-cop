"""Deterministic predictive police pursuit against a predicted thief set."""

from collections import deque

from salareen_cop.base_logic.state_types import Board, Coordinate

ORDER = (("N", -1, 0), ("S", 1, 0), ("E", 0, 1), ("W", 0, -1), ("STAY", 0, 0))
UNREACHABLE = 99
THREAT_RANGE = 1
RECENT_WINDOW = 6


def destinations(
    board: Board, origin: Coordinate, barriers: frozenset[Coordinate]
) -> tuple[Coordinate, ...]:
    """Return the legal orthogonal destinations, never counting STAY."""
    cells = []
    for _, row_delta, col_delta in ORDER[:4]:
        cell = Coordinate(origin.row + row_delta, origin.col + col_delta)
        if board.contains(cell) and cell not in barriers:
            cells.append(cell)
    return tuple(cells)


def distance_map(
    board: Board, origin: Coordinate, barriers: frozenset[Coordinate]
) -> dict[Coordinate, int]:
    """Return barrier-aware breadth-first distances from one origin."""
    distances = {origin: 0}
    pending = deque([origin])
    while pending:
        current = pending.popleft()
        for cell in destinations(board, current, barriers):
            if cell not in distances:
                distances[cell] = distances[current] + 1
                pending.append(cell)
    return distances


def predicted_cells(
    board: Board, thief: Coordinate, barriers: frozenset[Coordinate]
) -> tuple[Coordinate, ...]:
    """Return the thief estimate plus every legal one-step destination."""
    return (thief, *destinations(board, thief, barriers))


def recent_penalty(cell: Coordinate, history: object) -> int:
    """Count recent occupations of one cell inside the memory window."""
    if not isinstance(history, (list, tuple)) or not history:
        return 0
    return sum(1 for visited in history[-RECENT_WINDOW:] if visited == cell)


class PursuitPolicy:
    """Close on a predicted thief set without search, randomness, or clocks."""

    def __init__(self, board: Board) -> None:
        self.board = board

    def candidates(
        self, position: Coordinate, barriers: frozenset[Coordinate]
    ) -> tuple[tuple[str, Coordinate], ...]:
        """Return legal ``(choice, destination)`` pairs in fixed order."""
        options: list[tuple[str, Coordinate]] = []
        for name, row_delta, col_delta in ORDER:
            if name == "STAY":
                options.append((name, position))
                continue
            cell = Coordinate(position.row + row_delta, position.col + col_delta)
            if self.board.contains(cell) and cell not in barriers:
                options.append((name, cell))
        return tuple(options)

    def reach_maps(
        self, thief: Coordinate, barriers: frozenset[Coordinate]
    ) -> tuple[dict[Coordinate, int], ...]:
        """Return one barrier-aware distance map per predicted thief cell."""
        return tuple(
            distance_map(self.board, target, barriers)
            for target in predicted_cells(self.board, thief, barriers)
        )

    def rank(
        self,
        cell: Coordinate,
        index: int,
        reach: tuple[dict[Coordinate, int], ...],
        history: object,
    ) -> tuple[int, int, int, int, int]:
        """Rank one destination; lower is a strictly better pursuit move."""
        spread = [min(item.get(cell, UNREACHABLE), UNREACHABLE) for item in reach]
        threatened = sum(1 for value in spread if value <= THREAT_RANGE)
        return (
            max(spread),
            sum(spread),
            -threatened,
            recent_penalty(cell, history),
            index,
        )

    def choose(
        self,
        position: Coordinate,
        barriers: frozenset[Coordinate],
        thief: Coordinate | None,
        history: object = (),
    ) -> str:
        """Return one legal move choice; STAY is always a legal last resort."""
        options = self.candidates(position, barriers)
        if thief is None:
            return "STAY"
        for name, cell in options:
            if cell == thief:
                return name
        reach = self.reach_maps(thief, barriers)
        ranked = [
            (self.rank(cell, index, reach, history), name)
            for index, (name, cell) in enumerate(options)
        ]
        return min(ranked)[1]
