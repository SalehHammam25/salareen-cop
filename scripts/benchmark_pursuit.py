"""Local police benchmark: legacy greedy chase versus predictive pursuit."""

from __future__ import annotations

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from bench_thieves import EMITTERS, THIEVES  # noqa: E402

from salareen_cop.base_logic.state_types import Coordinate  # noqa: E402
from salareen_cop.official.engine import CopEngine  # noqa: E402
from salareen_cop.official.terms import TERMS  # noqa: E402
from salareen_cop.official.wire import clean_turn  # noqa: E402
from salareen_cop.pursuit.fallback import greedy_choice  # noqa: E402

STEPS = TERMS["max_steps"]
VARIANTS = (0, 1, 2, 3)
SEEDS = tuple(range(20))


class LegacyCop(CopEngine):
    """Reproduce the pre-change greedy scent-chasing decision rule exactly."""

    def _choice(self, message: dict) -> str:
        scent = (message or {}).get("smell_grid") or {}
        if not scent:
            target = Coordinate(*TERMS["thief_start"])
        else:
            key = max(scent, key=lambda item: (scent[item], item))
            row, col = (int(part) for part in key.split(","))
            target = Coordinate(row, col)
        return greedy_choice(self.board, self.position, frozenset(), 14, target)


def rings(pos):
    """Build the agreed 5x5 ring emission centred on one cell."""
    grid = {}
    for row in range(7):
        for col in range(7):
            ring = max(abs(row - pos[0]), abs(col - pos[1]))
            if ring < 3:
                grid[f"{row},{col}"] = (0.9, 0.6, 0.3)[ring]
    return grid


def message(step, grid):
    """Build one cleaned thief turn message from a prepared scent grid."""
    return clean_turn(
        {
            "step": step,
            "sender": "thief",
            "commit": f"{step:064x}",
            "hint": "",
            "smell_grid": grid,
            "timestamp": "",
            "barrier_placed": None,
            "capture_claim": None,
            "claim_response": None,
            "win_claim": None,
        }
    )


def play(factory, thief_move, seed, variant, emitter=None):
    """Run one episode; return (capture step or None, transcript)."""
    engine = factory(1, "1" * 40)
    rng = random.Random(seed)
    thief = tuple(TERMS["thief_start"])
    trail = []
    for step in range(1, STEPS + 1):
        thief = thief_move(thief, (engine.position.row, engine.position.col), rng, variant)
        police = (engine.position.row, engine.position.col)
        trail.append((thief, police))
        if thief == police:
            return step, tuple(trail)
        grid = rings(thief) if emitter is None else emitter(rings, thief, rng, variant)
        incoming = message(step, grid)
        engine.receive(incoming)
        engine.take_turn(incoming)
        police = (engine.position.row, engine.position.col)
        trail.append((thief, police))
        if police == thief:
            return step, tuple(trail)
    return None, tuple(trail)


def scenarios(name):
    """Return the (seed, variant) grid appropriate for one thief profile."""
    if name in {"random_legal", "spiky_emitter"}:
        return [(seed, 0) for seed in SEEDS]
    return [(0, variant) for variant in VARIANTS]


def summarise(factory, move, grid, emitter=None):
    """Return capture rate, median capture step, and distinct-game count."""
    runs = [play(factory, move, s, v, emitter) for s, v in grid]
    distinct = {trail for _, trail in runs}
    caught = sorted(step for step, _ in runs if step is not None)
    rate = 100 * len(caught) / len(runs)
    median = caught[len(caught) // 2] if caught else None
    return rate, median, len(distinct)


def main() -> int:
    print(f"{'benchmark thief':<22}{'distinct':>9}{'legacy':>18}{'pursuit':>18}")
    totals = [0, 0, 0]
    for name, move in THIEVES.items():
        grid = scenarios(name)
        emitter = EMITTERS.get(name)
        legacy = summarise(LegacyCop, move, grid, emitter)
        new = summarise(CopEngine, move, grid, emitter)
        distinct = max(legacy[2], new[2])
        cells = [
            f"{legacy[0]:5.0f}% cap step={legacy[1]}".rjust(18),
            f"{new[0]:5.0f}% cap step={new[1]}".rjust(18),
        ]
        print(f"{name:<22}{distinct:>9}" + "".join(cells))
        totals = [totals[0] + legacy[0], totals[1] + new[0], totals[2] + distinct]
    count = len(THIEVES)
    print(
        f"{'AGGREGATE':<22}{totals[2]:>9}"
        f"{totals[0] / count:17.0f}%{totals[1] / count:17.0f}%"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
