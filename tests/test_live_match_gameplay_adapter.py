from pathlib import Path

from salareen_cop.live_match.gameplay import GameplayAdapter
from salareen_cop.live_match.journal import Journal
from salareen_cop.live_match.session import LiveMatchSession

CONFIG = Path(__file__).parents[1] / "config" / "game.json"


def intent(**changes):
    value = {"protocol_version": "1.0-provisional", "correlation_id": "move-0",
             "sender_role": "thief", "game_id": "game", "session_id": "session",
             "game_number": 1, "turn_index": 0, "action_kind": "stay",
             "direction": "STAY", "x": None, "y": None}
    value.update(changes)
    return value


def test_session_applies_base_logic_and_restores_state(tmp_path):
    path = tmp_path / "cop.sqlite3"
    journal = Journal(path)
    gameplay = GameplayAdapter(CONFIG)
    session = LiveMatchSession("cop", "game", "session", 1, journal, gameplay)
    result = session.handle("submit_action_v1", intent())
    assert result["accepted"] and gameplay.state.valid_steps == 1
    saved = gameplay.snapshot()
    assert any(value for row in gameplay.scent.values for value in row)
    journal.close()
    recovered_journal = Journal(path)
    recovered = GameplayAdapter(
        CONFIG, recovered_journal.get_state("game", "session", "game_state")
    )
    assert recovered.snapshot() == saved


def test_rejected_action_preserves_state_and_scent(tmp_path):
    gameplay = GameplayAdapter(CONFIG)
    before, scent = gameplay.snapshot(), gameplay.scent
    session = LiveMatchSession("cop", "game", "session", 1,
                               Journal(tmp_path / "cop.sqlite3"), gameplay)
    result = session.handle("submit_action_v1", intent(
        action_kind="barrier", direction=None, x=3, y=4))
    assert not result["accepted"]
    assert gameplay.snapshot() == before and gameplay.scent == scent


def test_acknowledgement_applies_prepared_local_action_once(tmp_path):
    gameplay = GameplayAdapter(CONFIG)
    session = LiveMatchSession("cop", "game", "session", 1,
                               Journal(tmp_path / "cop.sqlite3"), gameplay)
    session.turn_index = 1
    local = intent(correlation_id="cop-1", sender_role="cop", turn_index=1,
                   action_kind="move", direction="S")
    assert session.prepare_local(local)["accepted"]
    acknowledgement = {"protocol_version": "1.0-provisional",
        "correlation_id": "ack-1", "sender_role": "thief", "game_id": "game",
        "session_id": "session", "game_number": 1, "turn_index": 1,
        "action_correlation_id": "cop-1", "result": "applied",
        "result_code": "OK", "next_turn_index": 2, "next_role": "thief"}
    first = session.handle("acknowledge_action_v1", acknowledgement)
    assert first["accepted"] and gameplay.state.valid_steps == 1
    assert session.handle("acknowledge_action_v1", acknowledgement) == first
    assert gameplay.state.valid_steps == 1
