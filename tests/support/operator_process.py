"""Process lifecycle primitives for the local two-peer gate."""

import json
import os
import socket
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path

PORTS = {"thief": 8801, "cop": 8802}


def events(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()]


def port_open(port: int) -> bool:
    with socket.socket() as probe:
        probe.settimeout(0.1)
        return probe.connect_ex(("127.0.0.1", port)) == 0


@dataclass
class Peer:
    role: str
    repo: Path
    runtime: Path
    scenario: str
    config: Path
    extra_env: dict[str, str] = field(default_factory=dict)
    process: subprocess.Popen | None = None

    @property
    def journal(self) -> Path:
        return self.runtime / f"{self.role}.sqlite3"

    @property
    def log(self) -> Path:
        return self.runtime / f"{self.role}.jsonl"

    def start(self) -> None:
        package = f"salareen_{self.role}"
        other = "cop" if self.role == "thief" else "thief"
        python = self.repo / ".venv" / "Scripts" / "python.exe"
        command = [str(python), "-m", f"{package}.live_match.runner",
                   "--host", "127.0.0.1", "--port", str(PORTS[self.role]),
                   "--opponent", f"http://127.0.0.1:{PORTS[other]}/mcp",
                   "--game-id", "gate-game", "--session-id", "gate-session",
                   "--scenario", self.scenario, "--config", str(self.config)]
        env = os.environ.copy()
        prefix = f"SALAREEN_{self.role.upper()}"
        env[f"{prefix}_JOURNAL"] = str(self.journal)
        env[f"{prefix}_EVENT_LOG"] = str(self.log)
        env.update({"SALAREEN_MAX_RETRIES": "20", "SALAREEN_RETRY_BACKOFF": "0.1"})
        env.update(self.extra_env)
        self.process = subprocess.Popen(command, cwd=self.repo, env=env,
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def stop(self, grace: float = 2) -> None:
        if not self.process or self.process.poll() is not None:
            return
        self.process.terminate()
        try:
            self.process.wait(grace)
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait(2)

    def wait_exit(self, timeout: float = 30) -> int:
        assert self.process
        return self.process.wait(timeout)


def wait_event(peer: Peer, kind: str, timeout: float = 15,
               correlation: str | None = None) -> dict:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        for item in events(peer.log):
            if item["event_type"] == kind and (
                    correlation is None or item["correlation_id"] == correlation):
                return item
        if peer.process and peer.process.poll() is not None:
            raise RuntimeError(f"{peer.role} exited before {kind}")
        time.sleep(0.02)
    raise TimeoutError(f"{peer.role} did not emit {kind}")


def assert_clean(peers: tuple[Peer, Peer]) -> None:
    for peer in peers:
        peer.stop()
    deadline = time.monotonic() + 3
    while time.monotonic() < deadline and any(port_open(port) for port in PORTS.values()):
        time.sleep(0.05)
    assert not any(port_open(port) for port in PORTS.values())
    assert all(peer.process is None or peer.process.poll() is not None for peer in peers)
