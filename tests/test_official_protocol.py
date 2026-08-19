import hashlib
import json

import pytest

from salareen_cop.official.delivery import DeliveryInbox, EquivocationError
from salareen_cop.official.engine import CopEngine
from salareen_cop.official.settlement import consensus_preimage, consensus_sha
from salareen_cop.official.terms import (
    TERMS,
    commit_of,
    derive_game_ids,
    greeting,
    terms_sha256,
)
from salareen_cop.official.wire import clean_turn, verify_greeting

COMMIT = "1" * 40
VECTOR_PAYLOAD = {
    "hint": "",
    "intent": "probe east",
    "move": "MOVE:E",
    "position": [3, 4],
    "role": "thief",
    "state": "ok",
    "step": 1,
    "sub_game": 1,
}


def turn(**changes):
    value = {
        "step": 1,
        "sender": "thief",
        "commit": "a" * 64,
        "hint": "",
        "smell_grid": {},
        "timestamp": "",
        "barrier_placed": None,
        "capture_claim": None,
        "claim_response": None,
        "win_claim": None,
    }
    value.update(changes)
    return value


def test_official_terms_vectors_and_ids():
    assert TERMS["setting"] == "Haifa" and len(TERMS) == 14
    assert terms_sha256() == "ad9e1bfd724e9debcde523833381cb7982a5d619d693d3738b59e0da61f4d81a"
    assert commit_of(VECTOR_PAYLOAD, "a" * 32) == (
        "4047830b8108320cbf48c1c1e1f09c6c0d47da51c225ce2cf40c7857cefc3030"
    )
    assert derive_game_ids("amireman", "salareen") == (
        "amireman-vs-salareen",
        "dc96f6d1-fc31-e0d9-3be2-05ddef48ed73",
    )


@pytest.mark.parametrize(
    "changes",
    [
        {"step": 1.0},
        {"step": True},
        {"step": -1},
        {"sender": ""},
        {"commit": "A" * 64},
        {"commit": "a" * 63},
    ],
)
def test_turn_hard_requirements(changes):
    assert clean_turn(turn(**changes)) is None


def test_optional_coordinates_and_scent_are_safely_cleaned():
    cleaned = clean_turn(
        turn(
            capture_claim=[3.0, 4],
            barrier_placed=[7, 0],
            smell_grid={"3,4": 0.9, "07,0": 0.2, "0,0": float("nan")},
        )
    )
    assert cleaned["capture_claim"] is None
    assert cleaned["barrier_placed"] is None
    assert cleaned["smell_grid"] == {"3,4": 0.9}


def test_fresh_signed_greeting_is_role_and_subgame_bound():
    peer = greeting("thief", 1, COMMIT, "salareen")
    peer["group_id"] = "amireman"
    peer["identity"]["group_id"] = "amireman"
    peer["game_uid"] = derive_game_ids("amireman", "salareen")[1]
    assert verify_greeting(peer, "thief", 1) == "amireman"
    with pytest.raises(ValueError):
        verify_greeting(peer, "police", 1)


def test_exactly_once_delivery_and_equivocation_detection():
    inbox = DeliveryInbox()
    message = turn()
    assert inbox.offer(message) == [message]
    assert inbox.offer(dict(message)) == []
    with pytest.raises(EquivocationError):
        inbox.offer(turn(commit="b" * 64))


def test_official_reference_consensus_shape_and_serialization():
    rows = [
        {
            "sub_game_number": 1,
            "result": "capture",
            "roles": {"amireman": "thief", "salareen": "police"},
            "score": {"amireman": 5, "salareen": 20},
            "winner_group": "salareen",
        }
    ]
    value = consensus_preimage("amireman-vs-salareen", rows)
    assert set(value) == {"game_id", "aggregate", "sub_games"}
    encoded = json.dumps(value, sort_keys=True, ensure_ascii=False)
    assert consensus_sha("amireman-vs-salareen", rows) == hashlib.sha256(
        encoded.encode("utf-8")
    ).hexdigest()


def test_cop_engine_uses_existing_policy_and_claims_every_turn():
    engine = CopEngine(1, COMMIT)
    message = engine.take_turn({"smell_grid": {"3,3": 0.9}})
    assert message["capture_claim"] == [1, 0]
    assert message["sender"] == "police"
    assert len(message["commit"]) == 64
