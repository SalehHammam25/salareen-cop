"""Scenario orchestration for the complete live-match gate."""

import json
from pathlib import Path

from gate_progress import run_case
from recovery_scenarios import negative, restart, terminal_restart


def run_scenarios(base, repeat, selected, make_peers, canonical, normal):
    scenarios = [
        "capture",
        "barrier_capture",
        "trapped",
        "capture_priority",
        "survival",
    ]
    outputs = {}
    for name in scenarios:
        if selected and selected != name:
            continue
        outputs[name] = [
            run_case(
                name,
                run,
                lambda run=run, name=name: normal(base / f"{name}-{run}", name),
            )
            for run in range(repeat)
        ]
    for name in ("ack_restart", "lost_ack"):
        if selected and selected != name:
            continue
        outputs[name] = [
            run_case(
                name,
                run,
                lambda run=run, name=name: restart(
                    base / f"{name}-{run}", name, make_peers, canonical
                ),
            )
            for run in range(repeat)
        ]
    for name in ("mismatch", "retry_exhaustion", "watchdog"):
        if selected and selected != name:
            continue
        outputs[name] = [
            run_case(
                name,
                run,
                lambda run=run, name=name: negative(
                    base / f"{name}-{run}", name, make_peers, canonical
                ),
            )
            for run in range(repeat)
        ]
    if not selected or selected == "terminal_restart":
        outputs["terminal_restart"] = [
            run_case(
                "terminal_restart",
                run,
                lambda run=run: terminal_restart(
                    base / f"terminal-{run}", make_peers, canonical
                ),
            )
            for run in range(repeat)
        ]
    ensure_repeatability(outputs)
    return outputs


def ensure_repeatability(outputs):
    mismatches = {
        name: values for name, values in outputs.items() if values[1:] != values[:-1]
    }
    if mismatches:
        detail = json.dumps(mismatches, indent=2, sort_keys=True)
        raise AssertionError("canonical mismatch:\n" + detail)


def prepare_runtime(root: Path, tempfile_module):
    (root / ".runtime").mkdir(exist_ok=True)
    return Path(tempfile_module.mkdtemp(prefix="live-gate-", dir=root / ".runtime"))
