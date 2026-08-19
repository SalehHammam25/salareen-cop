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
    generation: int = 0
    command: list[str] = field(default_factory=list)

    @property
    def journal(self) -> Path:
        return self.runtime / f"{self.role}.sqlite3"

    @property
    def log(self) -> Path:
        return self.runtime / f"{self.role}.jsonl"

    @property
    def stdout_path(self) -> Path:
        return self.runtime / f"{self.role}-{self.generation}.stdout.log"

    @property
    def stderr_path(self) -> Path:
        return self.runtime / f"{self.role}-{self.generation}.stderr.log"

    @property
    def pid(self) -> int | None:
        return None if self.process is None else self.process.pid

    @property
    def exit_code(self) -> int | None:
        return None if self.process is None else self.process.poll()

    def start(self) -> None:
        if self.process and self.process.poll() is None:
            raise RuntimeError(f"{self.role} process is already running")
        wait_port_closed(PORTS[self.role])
        self.generation += 1
        package = f"salareen_{self.role}"
        other = "cop" if self.role == "thief" else "thief"
        python = self.repo / ".venv" / "Scripts" / "python.exe"
        command = [
            str(python),
            "-m",
            f"{package}.live_match.runner",
            "--host",
            "127.0.0.1",
            "--port",
            str(PORTS[self.role]),
            "--opponent",
            f"http://127.0.0.1:{PORTS[other]}/mcp",
            "--game-id",
            "gate-game",
            "--session-id",
            "gate-session",
            "--scenario",
            self.scenario,
            "--config",
            str(self.config),
        ]
        self.command = command
        env = os.environ.copy()
        prefix = f"SALAREEN_{self.role.upper()}"
        env[f"{prefix}_JOURNAL"] = str(self.journal)
        env[f"{prefix}_EVENT_LOG"] = str(self.log)
        env.update(
            {
                "SALAREEN_MAX_RETRIES": "20",
                "SALAREEN_RETRY_BACKOFF": "0.1",
                "SALAREEN_RESPONSE_TIMEOUT": "3",
                "SALAREEN_WATCHDOG_TIMEOUT": "120",
            }
        )
        env.update(self.extra_env)
        with (
            self.stdout_path.open("a", encoding="utf-8") as stdout,
            self.stderr_path.open("a", encoding="utf-8") as stderr,
        ):
            self.process = subprocess.Popen(
                command, cwd=self.repo, env=env, stdout=stdout, stderr=stderr
            )

    def stop(self, grace: float = 2) -> str:
        if not self.process or self.process.poll() is not None:
            return "already_exited"
        self.process.terminate()
        try:
            self.process.wait(grace)
            action = "terminated"
        except subprocess.TimeoutExpired:
            self.process.kill()
            self.process.wait(2)
            action = "killed"
        wait_port_closed(PORTS[self.role])
        return action

    def wait_exit(self, timeout: float = 30) -> int:
        assert self.process
        return self.process.wait(timeout)


def wait_port_closed(port: int, timeout: float = 5) -> None:
    deadline = time.monotonic() + timeout
    while port_open(port) and time.monotonic() < deadline:
        time.sleep(0.02)
    if port_open(port):
        raise TimeoutError(f"port {port} remained bound")


def assert_clean(peers: tuple[Peer, Peer]) -> None:
    for peer in peers:
        peer.stop()
    deadline = time.monotonic() + 3
    while time.monotonic() < deadline and any(
        port_open(port) for port in PORTS.values()
    ):
        time.sleep(0.05)
    assert not any(port_open(port) for port in PORTS.values())
    assert all(
        peer.process is None or peer.process.poll() is not None for peer in peers
    )
