"""Focused tests for the deterministic predictive police pursuit policy."""

import inspect
from pathlib import Path

from salareen_cop.base_logic.actions import MoveChoice
from salareen_cop.base_logic.movement import target_for, validate_target
from salareen_cop.base_logic.state_types import Board, Coordinate
from salareen_cop.official.engine import CopEngine
from salareen_cop.official.wire import clean_turn
from salareen_cop.pursuit.fallback import greedy_choice
from salareen_cop.pursuit.policy import PursuitPolicy

BOARD = Board(7, 0, "top-left")
EMPTY: frozenset[Coordinate] = frozenset()
COMMIT = "1" * 40


def rings(cell: Coordinate) -> dict[str, float]:
    grid = {}
    for row in range(7):
        for col in range(7):
            ring = max(abs(row - cell.row), abs(col - cell.col))
            if ring < 3:
                grid[f"{row},{col}"] = (0.9, 0.6, 0.3)[ring]
    return grid


def turn(step: int, **changes) -> dict:
    value = {
        "step": step,
        "sender": "thief",
        "commit": f"{step:064x}",
        "hint": "",
        "smell_grid": {},
        "timestamp": "",
        "barrier_placed": None,
        "capture_claim": None,
        "claim_response": None,
        "win_claim": None,
    }
    value.update(changes)
    return clean_turn(value)


def test_intercepts_predicted_set_instead_of_one_stale_cell() -> None:
    police, thief = Coordinate(0, 0), Coordinate(1, 4)
    assert greedy_choice(BOARD, police, EMPTY, 14, thief) == "S"
    assert PursuitPolicy(BOARD).choose(police, EMPTY, thief, []) == "E"


def test_every_choice_minimises_the_predicted_set_ranking() -> None:
    policy = PursuitPolicy(BOARD)
    for row in range(7):
        for col in range(7):
            police, thief = Coordinate(row, col), Coordinate(3, 3)
            if police == thief:
                continue
            options = policy.candidates(police, EMPTY)
            reach = policy.reach_maps(thief, EMPTY)
            ranks = [
                (policy.rank(cell, index, reach, []), name)
                for index, (name, cell) in enumerate(options)
            ]
            assert policy.choose(police, EMPTY, thief, []) == min(ranks)[1]


def test_immediate_capture_is_taken_before_any_ranking() -> None:
    policy = PursuitPolicy(BOARD)
    assert policy.choose(Coordinate(3, 3), EMPTY, Coordinate(3, 4), []) == "E"
    assert policy.choose(Coordinate(3, 3), EMPTY, Coordinate(2, 3), []) == "N"


def test_captures_a_stationary_target() -> None:
    engine = CopEngine(1, COMMIT)
    thief = Coordinate(3, 3)
    for step in range(1, 36):
        incoming = turn(step, smell_grid=rings(thief))
        engine.receive(incoming)
        engine.take_turn(incoming)
        if engine.position == thief:
            assert step <= 12
            return
    raise AssertionError("stationary target was never captured")


def test_every_selected_move_is_legal_everywhere() -> None:
    policy = PursuitPolicy(BOARD)
    barriers = frozenset({Coordinate(2, 2), Coordinate(2, 3), Coordinate(3, 2)})
    for row in range(7):
        for col in range(7):
            police = Coordinate(row, col)
            if police in barriers:
                continue
            for thief in (Coordinate(0, 6), Coordinate(6, 0), Coordinate(4, 4)):
                name = policy.choose(police, barriers, thief, [police])
                target = target_for(police, MoveChoice(name))
                assert validate_target(BOARD, police, target, barriers) is None


def test_policy_is_total_and_legal_over_a_wide_state_sweep() -> None:
    policy = PursuitPolicy(BOARD)
    cells = [Coordinate(row, col) for row in range(7) for col in range(7)]
    barrier_sets = (
        EMPTY,
        frozenset({Coordinate(3, col) for col in range(7)}),
        frozenset(
            cell
            for cell in cells
            if (cell.row + cell.col) % 2 == 0 and cell != Coordinate(0, 0)
        ),
    )
    seen = 0
    for barriers in barrier_sets:
        free = [cell for cell in cells if cell not in barriers]
        for police in free:
            for thief in (*free[::5], None):
                name = policy.choose(police, barriers, thief, [police, police])
                assert name in {"N", "S", "E", "W", "STAY"}
                target = target_for(police, MoveChoice(name))
                assert validate_target(BOARD, police, target, barriers) is None
                seen += 1
    assert seen > 500


def test_production_engine_keeps_no_broad_strategy_fallback() -> None:
    source = Path(inspect.getfile(CopEngine)).read_text(encoding="utf-8")
    assert "except" not in source
    assert "fallback" not in source
