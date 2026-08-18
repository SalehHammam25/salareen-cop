from salareen_cop.live_match.endpoints import validate_endpoint
from salareen_cop.live_match.journal import Journal
from salareen_cop.live_match.session import LiveMatchSession


def action(**changes):
    value = {
        "protocol_version": "1.0-provisional",
        "correlation_id": "a-0",
        "sender_role": "thief",
        "game_id": "game",
        "session_id": "session",
        "game_number": 1,
        "turn_index": 0,
        "action_kind": "stay",
        "direction": "STAY",
        "x": None,
        "y": None,
    }
    value.update(changes)
    return value


def test_action_is_exactly_once_and_durable(tmp_path):
    path = tmp_path / "cop.sqlite3"
    journal = Journal(path)
    session = LiveMatchSession("cop", "game", "session", 1, journal)
    first = session.handle("submit_action_v1", action())
    assert first == session.handle("submit_action_v1", action())
    assert session.applied_actions == 1
    mismatch = session.handle("submit_action_v1", action(direction="N"))
    assert mismatch["code"] == "DUPLICATE_MISMATCH"
    journal.close()
    recovered = LiveMatchSession("cop", "game", "session", 1, Journal(path))
    assert recovered.applied_actions == 1
    assert recovered.handle("submit_action_v1", action()) == first
    assert recovered.applied_actions == 1


def test_expected_role_and_strict_shape(tmp_path):
    session = LiveMatchSession(
        "cop", "game", "session", 1, Journal(tmp_path / "cop.sqlite3")
    )
    assert session.handle("submit_action_v1", action(sender_role="cop"))["code"] == (
        "WRONG_EXPECTED_ROLE"
    )
    assert (
        session.handle("submit_action_v1", action(extra=True))["code"]
        == "UNKNOWN_FIELD"
    )


def test_endpoint_policy():
    assert validate_endpoint(
        "http://127.0.0.1:8801/mcp", mode="local", host="127.0.0.1", permitted_port=8801
    )
    for url in (
        "https://peer.example/mcp?q=x",
        "https://127.0.0.1:443/mcp",
        "https://peer.example/wrong",
    ):
        try:
            validate_endpoint(
                url, mode="remote", host="peer.example", permitted_port=443
            )
        except ValueError:
            pass
        else:
            raise AssertionError(url)
