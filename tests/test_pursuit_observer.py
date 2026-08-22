"""Focused tests for police thief-estimation from cleaned wire scent."""

from salareen_cop.base_logic.state_types import Board, Coordinate
from salareen_cop.official.engine import CopEngine
from salareen_cop.official.wire import clean_turn
from salareen_cop.pursuit.observer import ThiefObserver
from salareen_cop.pursuit.policy import PursuitPolicy, predicted_cells

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


def test_malformed_empty_and_impossible_scent_are_safe() -> None:
    observer = ThiefObserver(BOARD, Coordinate(3, 3))
    for payload in (
        None,
        {},
        {"smell_grid": None},
        {"smell_grid": "not-a-grid"},
        {"smell_grid": {}},
        {"smell_grid": {"a,b": 0.9}},
        {"smell_grid": {"9,9": 0.9}},
        {"smell_grid": {"3": 0.9}},
        {"smell_grid": {"0,0": True}},
        {"smell_grid": {"0,0": "high"}},
    ):
        assert BOARD.contains(observer.update(payload))
    assert observer.estimate == Coordinate(3, 3)


def test_impossible_jumps_are_rejected_then_allowed_as_evidence_ages() -> None:
    observer = ThiefObserver(BOARD, Coordinate(3, 3))
    assert observer.update({"smell_grid": {"0,0": 0.9}}) == Coordinate(3, 3)
    assert observer.update({"smell_grid": {"3,4": 0.9}}) == Coordinate(3, 4)
    for _ in range(11):
        observer.update({})
    assert observer.update({"smell_grid": {"0,0": 0.9}}) == Coordinate(0, 0)


def test_recent_cells_are_penalised_in_the_ranking() -> None:
    policy = PursuitPolicy(BOARD)
    reach = policy.reach_maps(Coordinate(0, 3), EMPTY)
    cell = Coordinate(3, 4)
    fresh = policy.rank(cell, 2, reach, [])
    seen = policy.rank(cell, 2, reach, [cell, cell])
    assert seen > fresh
    assert fresh[:3] == seen[:3]
    assert fresh[3] == 0 and seen[3] == 2


def test_a_legally_oscillating_thief_is_closed_down_not_mirrored() -> None:
    engine = CopEngine(1, COMMIT)
    cells = (Coordinate(6, 6), Coordinate(6, 5))
    for step in range(1, 36):
        thief = cells[step % 2]
        incoming = turn(step, smell_grid=rings(thief))
        engine.receive(incoming)
        engine.take_turn(incoming)
        if engine.position == thief:
            assert step <= 20
            return
    raise AssertionError("oscillating thief was never captured")


def test_repeated_runs_produce_identical_decisions() -> None:
    def transcript() -> list[str]:
        engine = CopEngine(1, COMMIT)
        moves = []
        for step in range(1, 20):
            incoming = turn(step, smell_grid=rings(Coordinate(step % 7, 6)))
            engine.receive(incoming)
            engine.take_turn(incoming)
            moves.append(engine.records[-1]["payload"]["move"])
        return moves

    assert transcript() == transcript()


def test_only_cleaned_wire_information_reaches_the_estimate() -> None:
    engine = CopEngine(1, COMMIT)
    incoming = turn(1, smell_grid={"3,4": 0.9})
    engine.receive(incoming)
    engine.take_turn(incoming)
    assert engine.observer.estimate == Coordinate(3, 4)
    assert not hasattr(engine, "thief")


def test_predicted_cells_are_the_estimate_plus_legal_steps() -> None:
    cells = predicted_cells(BOARD, Coordinate(0, 0), EMPTY)
    assert set(cells) == {Coordinate(0, 0), Coordinate(1, 0), Coordinate(0, 1)}
