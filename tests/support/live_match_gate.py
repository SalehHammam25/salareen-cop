"""Reusable complete local pre-ngrok process verification harness."""

import argparse
import json
import tempfile
from pathlib import Path

from gate_progress import run_case
from operator_process import Peer, assert_clean, events
from process_diagnostics import wait_ready, wait_success
from recovery_scenarios import negative, restart, terminal_restart

HERE = Path(__file__).resolve()
ROOT = HERE.parents[3]
REPOS = {role: ROOT / f"salareen-{role}" for role in ("cop", "thief")}


def priority_config(runtime: Path) -> Path:
    source = REPOS["cop"] / "config" / "game.json"
    data = json.loads(source.read_text(encoding="utf-8"))
    movement = data["movement_and_barriers"]
    movement["max_moves"] = movement["survival_threshold"] = 36
    target = runtime / "capture-priority.json"
    target.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    return target


def make_peers(runtime: Path, scenario: str, envs=None) -> tuple[Peer, Peer]:
    runtime.mkdir(parents=True, exist_ok=False)
    config = (priority_config(runtime) if scenario == "capture_priority" else
              REPOS["cop"] / "config" / "game.json")
    envs = envs or {}
    thief = Peer("thief", REPOS["thief"], runtime, scenario, config,
                 envs.get("thief", {}))
    cop = Peer("cop", REPOS["cop"], runtime, scenario, config, envs.get("cop", {}))
    return thief, cop


def start(peers: tuple[Peer, Peer]) -> None:
    thief, cop = peers
    thief.start()
    wait_ready(thief)
    cop.start()
    wait_ready(cop)


def canonical(peers: tuple[Peer, Peer]) -> dict:
    all_events = events(peers[0].log) + events(peers[1].log)
    action_ids = {item["correlation_id"] for item in all_events
                  if item["event_type"] == "action_applied"}
    ordered = sorted(action_ids, key=lambda value: int(value.split("-")[1]))
    decisions = sorted({(item["local_role"], item["event_type"],
                         item["correlation_id"], item["turn_index"])
        for item in all_events if item["event_type"] in {
            "duplicate_replayed", "resume_accepted", "recovery_rejected",
            "recovery_exhausted", "watchdog_expired"}})
    terminal = next((item["data"] for item in reversed(events(peers[1].log))
                     if item["event_type"] == "terminal_agreed"), {})
    score = next((item["data"] for item in reversed(events(peers[1].log))
                  if item["event_type"] == "score_agreed"), {})
    applied = {peer.role: len({item["correlation_id"] for item in events(peer.log)
                               if item["event_type"] == "action_applied"})
               for peer in peers}
    return {"actions": ordered, "terminal": terminal.get("outcome"),
            "score": [score.get("cop_score"), score.get("thief_score")],
            "decisions": decisions, "application_counts": applied}


def normal(runtime: Path, scenario: str) -> dict:
    peers = make_peers(runtime, scenario)
    try:
        start(peers)
        wait_success(peers, 120)
        result = canonical(peers)
        expected = "thief_survival" if scenario == "survival" else "cop_capture"
        assert result["terminal"] == expected
        assert result["score"] == ([5, 10] if scenario == "survival" else [20, 5])
        return result
    finally:
        assert_clean(peers)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repeat", type=int, default=2)
    parser.add_argument("--scenario")
    args = parser.parse_args()
    scenarios = ["capture", "barrier_capture", "trapped", "capture_priority", "survival"]
    outputs: dict[str, list[dict]] = {}
    (ROOT / ".runtime").mkdir(exist_ok=True)
    base = Path(tempfile.mkdtemp(prefix="live-gate-", dir=ROOT / ".runtime"))
    print(f"runtime={base}", flush=True)
    try:
        for name in scenarios:
            if args.scenario and args.scenario != name:
                continue
            outputs[name] = [run_case(name, run, lambda run=run, name=name:
                normal(base / f"{name}-{run}", name)) for run in range(args.repeat)]
        for name in ("ack_restart", "lost_ack"):
            if args.scenario and args.scenario != name:
                continue
            outputs[name] = [run_case(name, run, lambda run=run, name=name:
                restart(base / f"{name}-{run}", name, make_peers, canonical))
                for run in range(args.repeat)]
        for name in ("mismatch", "retry_exhaustion", "watchdog"):
            if args.scenario and args.scenario != name:
                continue
            outputs[name] = [run_case(name, run, lambda run=run, name=name:
                negative(base / f"{name}-{run}", name, make_peers, canonical))
                for run in range(args.repeat)]
        if not args.scenario or args.scenario == "terminal_restart":
            outputs["terminal_restart"] = [run_case("terminal_restart", run,
                lambda run=run: terminal_restart(base / f"terminal-{run}",
                                                  make_peers, canonical))
                for run in range(args.repeat)]
    finally:
        print(f"runtime={base}", flush=True)
    mismatches = {name: values for name, values in outputs.items()
                  if values[1:] != values[:-1]}
    if mismatches:
        raise AssertionError("canonical mismatch:\n" + json.dumps(
            mismatches, indent=2, sort_keys=True))
    print(json.dumps({key: value[0] for key, value in outputs.items()}, sort_keys=True))


if __name__ == "__main__":
    main()
