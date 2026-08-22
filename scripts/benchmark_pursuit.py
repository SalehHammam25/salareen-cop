"""Small deterministic police benchmark: legacy greedy versus predictive pursuit."""

from __future__ import annotations

import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from salareen_cop.base_logic.state_types import Coordinate  # noqa: E402
from salareen_cop.official.engine import CopEngine  # noqa: E402
from salareen_cop.official.terms import TERMS  # noqa: E402
from salareen_cop.official.wire import clean_turn  # noqa: E402
from salareen_cop.pursuit.fallback import greedy_choice  # noqa: E402

DELTAS = ((-1, 0), (1, 0), (0, 1), (0, -1))
STEPS = TERMS["max_steps"]


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


def legal(cell):
    return [
        (cell[0] + dr, cell[1] + dc)
        for dr, dc in DELTAS
        if 0 <= cell[0] + dr < 7 and 0 <= cell[1] + dc < 7
    ]


def distance(left, right):
    return abs(left[0] - right[0]) + abs(left[1] - right[1])


def stationary(pos, foe, rng):
    return pos


def flee(pos, foe, rng):
    return max([pos, *legal(pos)], key=lambda c: (distance(c, foe), -c[0], -c[1]))


def random_legal(pos, foe, rng):
    return rng.choice([pos, *legal(pos)])


def mobility(pos, foe, rng):
    options = [pos, *legal(pos)]
    return max(options, key=lambda c: (len(legal(c)), distance(c, foe), -c[0], -c[1]))


THIEVES = {
    "stationary": stationary,
    "run_away": flee,
    "random_legal": random_legal,
    "mobility_max": mobility,
}


def rings(pos):
    grid = {}
    for row in range(7):
        for col in range(7):
            ring = max(abs(row - pos[0]), abs(col - pos[1]))
            if ring < 3:
                grid[f"{row},{col}"] = (0.9, 0.6, 0.3)[ring]
    return grid


def message(step, thief):
    return clean_turn(
        {
            "step": step,
            "sender": "thief",
            "commit": f"{step:064x}",
            "hint": "",
            "smell_grid": rings(thief),
            "timestamp": "",
            "barrier_placed": None,
            "capture_claim": None,
            "claim_response": None,
            "win_claim": None,
        }
    )


def play(factory, thief_move, seed):
    """Run one deterministic episode; return the capture step or None."""
    engine = factory(1, "1" * 40)
    rng = random.Random(seed)
    thief = tuple(TERMS["thief_start"])
    for step in range(1, STEPS + 1):
        thief = thief_move(thief, (engine.position.row, engine.position.col), rng)
        if thief == (engine.position.row, engine.position.col):
            return step
        incoming = message(step, thief)
        engine.receive(incoming)
        engine.take_turn(incoming)
        if (engine.position.row, engine.position.col) == thief:
            return step
    return None


def main() -> int:
    seeds = tuple(range(20))
    print(f"{'thief':<14}{'legacy':>18}{'pursuit':>18}")
    for name, move in THIEVES.items():
        row = [name.ljust(14)]
        for factory in (LegacyCop, CopEngine):
            results = [play(factory, move, seed) for seed in seeds]
            caught = [value for value in results if value is not None]
            rate = 100 * len(caught) / len(results)
            median = sorted(caught)[len(caught) // 2] if caught else None
            row.append(f"{rate:5.0f}% cap  step={median}".rjust(18))
        print("".join(row))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
