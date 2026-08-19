"""Detailed Windows subprocess failure evidence."""

import json
import time
from pathlib import Path

from operator_process import PORTS, events, port_open


def tail(path: Path, count: int = 12) -> list[str]:
    if not path.exists():
        return []
    return path.read_text(encoding="utf-8", errors="replace").splitlines()[-count:]


def snapshot(peer, *, timed_out: bool, cleanup: str = "none") -> dict:
    history = events(peer.log)
    last = history[-1] if history else None
    return {
        "role": peer.role,
        "pid": peer.pid,
        "exit_code": peer.exit_code,
        "command": peer.command,
        "timed_out": timed_out,
        "last_event": last,
        "stdout_tail": tail(peer.stdout_path),
        "stderr_tail": tail(peer.stderr_path),
        "bound_port": PORTS[peer.role] if port_open(PORTS[peer.role]) else None,
        "cleanup_action": cleanup,
    }


def wait_success(peers, timeout: float) -> None:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if all(peer.exit_code is not None for peer in peers):
            break
        time.sleep(0.02)
    timed_out = {peer.role: peer.exit_code is None for peer in peers}
    failed = any(timed_out.values()) or any(
        peer.exit_code not in {0, None} for peer in peers
    )
    if not failed:
        return
    cleanup = {peer.role: peer.stop() for peer in peers}
    report = [
        snapshot(peer, timed_out=timed_out[peer.role], cleanup=cleanup[peer.role])
        for peer in peers
    ]
    raise AssertionError(
        "peer lifecycle failure:\n" + json.dumps(report, indent=2, sort_keys=True)
    )


def wait_exit(peer, timeout: float, *, fallback: bool = False) -> int:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        if peer.exit_code is not None:
            return peer.exit_code
        time.sleep(0.02)
    action = peer.stop()
    report = snapshot(peer, timed_out=True, cleanup=action)
    if fallback:
        print("peer_cleanup=" + json.dumps(report, sort_keys=True), flush=True)
        return peer.exit_code if peer.exit_code is not None else -1
    raise AssertionError(
        "peer exit timeout:\n" + json.dumps(report, indent=2, sort_keys=True)
    )


def wait_event(
    peer, kind: str, timeout: float = 15, correlation: str | None = None
) -> dict:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        for item in events(peer.log):
            if item["event_type"] == kind and (
                correlation is None or item["correlation_id"] == correlation
            ):
                return item
        if peer.exit_code is not None:
            report = snapshot(peer, timed_out=False)
            raise AssertionError(
                f"{peer.role} exited before {kind}:\n"
                + json.dumps(report, indent=2, sort_keys=True)
            )
        time.sleep(0.02)
    report = snapshot(peer, timed_out=True)
    raise AssertionError(
        f"{peer.role} did not emit {kind}:\n"
        + json.dumps(report, indent=2, sort_keys=True)
    )


def wait_ready(peer, timeout: float = 120) -> None:
    try:
        wait_event(peer, "server_ready", timeout)
    except AssertionError as error:
        cleanup = peer.stop()
        report = snapshot(peer, timed_out=True, cleanup=cleanup)
        raise AssertionError(
            "server readiness failed:\n" + json.dumps(report, indent=2, sort_keys=True)
        ) from error
    deadline = time.monotonic() + timeout
    consecutive = 0
    while time.monotonic() < deadline:
        if peer.exit_code is not None:
            report = snapshot(peer, timed_out=False)
            raise AssertionError(
                "peer exited during readiness:\n"
                + json.dumps(report, indent=2, sort_keys=True)
            )
        consecutive = consecutive + 1 if port_open(PORTS[peer.role]) else 0
        if consecutive >= 2:
            return
        time.sleep(0.02)
    report = snapshot(peer, timed_out=True)
    raise AssertionError(
        "port readiness failed:\n" + json.dumps(report, indent=2, sort_keys=True)
    )
