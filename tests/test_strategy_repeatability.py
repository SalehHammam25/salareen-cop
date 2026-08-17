"""Fresh-process strategy repeatability."""

import subprocess
import sys

from salareen_cop.base_logic.state_types import Coordinate
from salareen_cop.strategy.blind import BlindCopPolicy
from salareen_cop.strategy.models import snapshot_for


def test_repeated_snapshot_is_identical(initial_game) -> None:
    snapshot = snapshot_for(initial_game, Coordinate(4, 4))
    assert BlindCopPolicy().propose(snapshot) == BlindCopPolicy().propose(snapshot)


def test_fresh_process_tie_is_identical() -> None:
    script = (
        "from salareen_cop.base_logic.state_types import *; "
        "from salareen_cop.strategy.blind import BlindCopPolicy; "
        "from salareen_cop.strategy.models import StrategySnapshot; "
        "s=StrategySnapshot(Board(7,0,'top-left'),Coordinate(3,3),frozenset(),"
        "14,EpisodeStatus.ACTIVE,Coordinate(4,4)); "
        "print(BlindCopPolicy().propose(s))"
    )
    outputs = [
        subprocess.run(
            [sys.executable, "-c", script],
            capture_output=True,
            text=True,
            check=True,
        ).stdout
        for _ in range(2)
    ]
    assert outputs[0] == outputs[1]
