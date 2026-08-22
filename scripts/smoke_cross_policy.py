"""Local cross-policy smoke over the real cleaned-wire boundary. No network."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "salareen-cop" / "src"))
sys.path.insert(0, str(ROOT / "salareen-thief" / "src"))

from salareen_thief.evasion.fallback import corner_choice  # noqa: E402
from salareen_thief.official.engine import ThiefEngine  # noqa: E402

from salareen_cop.base_logic.state_types import Coordinate  # noqa: E402
from salareen_cop.official.engine import CopEngine  # noqa: E402
from salareen_cop.official.terms import TERMS  # noqa: E402
from salareen_cop.official.wire import clean_turn  # noqa: E402
from salareen_cop.pursuit.fallback import greedy_choice  # noqa: E402

DELTAS = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1), "STAY": (0, 0)}


class LegacyCop(CopEngine):
    """Pre-change greedy scent chase, for comparison only."""

    def _choice(self, message: dict) -> str:
        scent = (message or {}).get("smell_grid") or {}
        if not scent:
            target = Coordinate(*TERMS["thief_start"])
        else:
            key = max(scent, key=lambda item: (scent[item], item))
            row, col = (int(part) for part in key.split(","))
            target = Coordinate(row, col)
        return greedy_choice(self.board, self.position, frozenset(), 14, target)


class LegacyThief(ThiefEngine):
    """Pre-change corner-seeking evasion, for comparison only."""

    def _choice(self) -> str:
        return corner_choice(
            self.board, self.position, frozenset(self.barriers), self.last_threat
        )


def check_record(engine, before, label, issues):
    """Assert the committed move description matches the realised displacement."""
    payload = engine.records[-1]["payload"]
    move = payload["move"]
    name = "STAY" if move == "STAY" else move.split(":", 1)[1]
    if name not in DELTAS:
        issues.append(f"{label}: unknown move {move!r}")
        return
    row, col = DELTAS[name]
    expected = (before.row + row, before.col + col)
    actual = (engine.position.row, engine.position.col)
    if actual != expected:
        issues.append(f"{label}: recorded {move} but moved {before}->{actual}")
    if payload["position"] != list(actual):
        issues.append(f"{label}: payload position disagrees with engine position")


def run(cop_class, thief_class):
    """Play one full local episode and return a result summary."""
    cop, thief = cop_class(1, "1" * 40), thief_class(1, "1" * 40)
    issues, trail, outcome = [], [], "survival"
    incoming = None
    for step in range(1, TERMS["max_steps"] + 1):
        before = thief.position
        raw = thief.take_turn(incoming)
        check_record(thief, before, f"thief step {step}", issues)
        clean = clean_turn(raw)
        if clean is None:
            issues.append(f"thief step {step}: malformed payload")
            break
        outcome_in = cop.receive(clean)
        if outcome_in.won:
            outcome = "capture"
            break
        before = cop.position
        raw = cop.take_turn(clean)
        check_record(cop, before, f"cop step {step}", issues)
        incoming = clean_turn(raw)
        if incoming is None:
            issues.append(f"cop step {step}: malformed payload")
            break
        trail.append(
            (
                (thief.position.row, thief.position.col),
                (cop.position.row, cop.position.col),
                thief.step,
                cop.step,
            )
        )
        if thief.receive(incoming).caught:
            thief.take_turn(incoming, hold=True)
            outcome = "capture"
            break
    return outcome, len(trail), tuple(trail), issues


def main() -> int:
    pairs = (
        ("new police vs new thief", CopEngine, ThiefEngine),
        ("new police vs legacy thief", CopEngine, LegacyThief),
        ("legacy police vs new thief", LegacyCop, ThiefEngine),
    )
    failures = 0
    print(f"{'matchup':<30}{'outcome':>10}{'turns':>7}{'repeat':>9}{'steps':>8}{'issues':>8}")
    for label, cop_class, thief_class in pairs:
        outcome, turns, trail, issues = run(cop_class, thief_class)
        again = run(cop_class, thief_class)
        repeat = "same" if again[2] == trail and again[0] == outcome else "DIFFERS"
        steps = "ok" if all(
            item[2] == index + 1 and item[3] == index + 1
            for index, item in enumerate(trail)
        ) else "BROKEN"
        failures += len(issues) + (repeat != "same") + (steps != "ok")
        print(f"{label:<30}{outcome:>10}{turns:>7}{repeat:>9}{steps:>8}{len(issues):>8}")
        for issue in issues:
            print(f"    ! {issue}")
    print("SMOKE OK" if failures == 0 else f"SMOKE FAILURES: {failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
