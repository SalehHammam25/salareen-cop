"""Focused tests that a self-referential scent peak cannot freeze the police."""

from salareen_cop.base_logic.actions import MoveChoice
from salareen_cop.base_logic.movement import target_for, validate_target
from salareen_cop.base_logic.state_types import Board, Coordinate
from salareen_cop.official.engine import CopEngine
from salareen_cop.official.wire import clean_turn
from salareen_cop.pursuit.policy import PursuitPolicy

BOARD = Board(7, 0, "top-left")
EMPTY: frozenset[Coordinate] = frozenset()
COMMIT = "1" * 40
POLICY = PursuitPolicy(BOARD)


def rings(cell: Coordinate) -> dict[str, float]:
    grid = {}
    for row in range(7):
        for col in range(7):
            ring = max(abs(row - cell.row), abs(col - cell.col))
            if ring < 3:
                grid[f"{row},{col}"] = (0.9, 0.6, 0.3)[ring]
    return grid


def turn(step: int, peak: Coordinate) -> dict:
    return clean_turn(
        {
            "step": step,
            "sender": "thief",
            "commit": f"{step:064x}",
            "hint": "",
            "smell_grid": rings(peak),
            "timestamp": "",
            "barrier_placed": None,
            "capture_claim": None,
            "claim_response": None,
            "win_claim": None,
        }
    )


def test_own_cell_estimate_never_returns_stay() -> None:
    for row in range(7):
        for col in range(7):
            here = Coordinate(row, col)
            assert POLICY.choose(here, EMPTY, here, [here]) != "STAY"


def test_own_cell_estimate_still_returns_a_legal_move() -> None:
    for row in range(7):
        for col in range(7):
            here = Coordinate(row, col)
            name = POLICY.choose(here, EMPTY, here, [here, here])
            target = target_for(here, MoveChoice(name))
            assert validate_target(BOARD, here, target, EMPTY) is None


def test_a_fully_walled_police_may_still_stay() -> None:
    here = Coordinate(0, 0)
    barriers = frozenset({Coordinate(1, 0), Coordinate(0, 1)})
    assert POLICY.choose(here, barriers, here, [here]) == "STAY"


def test_a_peak_walked_onto_the_police_cannot_freeze_it() -> None:
    engine = CopEngine(1, COMMIT)
    peak = Coordinate(3, 3)
    visited = []
    for step in range(1, 26):
        police = engine.position
        row = peak.row + (1 if peak.row < police.row else -1 if peak.row > police.row else 0)
        col = peak.col if row != peak.row else (
            peak.col + (1 if peak.col < police.col else -1 if peak.col > police.col else 0)
        )
        peak = Coordinate(row, col)
        incoming = turn(step, peak)
        engine.receive(incoming)
        engine.take_turn(incoming)
        visited.append(engine.position)
    assert len(set(visited[-10:])) >= 2
    assert not any(
        visited[index] == visited[index + 1] == visited[index + 2]
        for index in range(len(visited) - 2)
    )


def test_the_freeze_attack_is_deterministic() -> None:
    def transcript() -> list[str]:
        engine = CopEngine(1, COMMIT)
        moves = []
        for step in range(1, 20):
            incoming = turn(step, engine.position)
            engine.receive(incoming)
            engine.take_turn(incoming)
            moves.append(engine.records[-1]["payload"]["move"])
        return moves

    first = transcript()
    assert first == transcript()
    assert "STAY" not in first


def test_genuine_capture_claim_and_response_semantics_are_unchanged() -> None:
    engine = CopEngine(1, COMMIT)
    message = engine.take_turn(turn(1, Coordinate(3, 3)))
    assert message["capture_claim"] == [engine.position.row, engine.position.col]
    assert message["barrier_placed"] is None
    assert set(message) == {
        "step",
        "sender",
        "commit",
        "hint",
        "smell_grid",
        "timestamp",
        "barrier_placed",
        "capture_claim",
        "claim_response",
        "win_claim",
    }
    reply = {"claim": message["capture_claim"], "caught": True}
    assert engine.receive({"claim_response": reply}).won is True


def test_moving_onto_a_distinct_estimate_is_still_an_immediate_capture() -> None:
    here = Coordinate(3, 3)
    assert POLICY.choose(here, EMPTY, Coordinate(2, 3), []) == "N"
    assert POLICY.choose(here, EMPTY, Coordinate(3, 4), []) == "E"
