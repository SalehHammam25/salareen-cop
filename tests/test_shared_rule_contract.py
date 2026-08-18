"""Cross-repository Stage 1 contract audit without importing thief code."""

import json
from pathlib import Path

from salareen_cop.base_logic.actions import MoveChoice
from salareen_cop.base_logic.config_results import ConfigAccepted
from salareen_cop.base_logic.config_validation import validate_config
from salareen_cop.base_logic.state_types import CaptureCause, Role


def test_committed_fixture_matches_shared_annex_f_contract() -> None:
    data = json.loads(Path("config/game.json").read_text(encoding="utf-8"))
    assert data["board_and_agents"] == {
        "grid_size": 7,
        "num_agents": 2,
        "thief_start": [3, 3],
        "cop_start": [0, 0],
        "axis_origin_corner": "top-left",
        "axis_start_index": 0,
    }
    assert data["movement_and_barriers"] == {
        "move_set": ["N", "S", "E", "W", "STAY"],
        "max_barriers": 14,
        "max_moves": 35,
        "survival_threshold": 35,
    }
    assert data["scoring"] == {
        "capture_cop": 20,
        "capture_thief": 5,
        "survival_cop": 5,
        "survival_thief": 10,
        "tie_score": 2,
        "technical_loss": 0,
    }
    assert isinstance(validate_config(data), ConfigAccepted)


def test_shared_enumerated_vocabulary_is_exact() -> None:
    assert tuple(MoveChoice) == ("N", "S", "E", "W", "STAY")
    assert tuple(Role) == ("thief", "cop")
    assert tuple(CaptureCause) == (
        "coordinate_overlap",
        "barrier_on_thief",
        "trapped_thief",
    )
