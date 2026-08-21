"""The runner refuses a remote series unless every new-match argument is safe.

Every case here must fail during argument validation, so no server, tunnel or
match is ever started by this module.
"""

import subprocess
import sys

import pytest

RUNNER = "salareen_cop.official.runner"
OPPONENT = "https://opponent.example/mcp"
BASE = [
    "--opponent",
    OPPONENT,
    "--police-commit",
    "1" * 40,
    "--thief-commit",
    "2" * 40,
]


def _run(*extra: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", RUNNER, *BASE, *extra],
        capture_output=True,
        text=True,
        timeout=120,
    )


def test_runner_exposes_the_new_opponent_group_flag():
    result = subprocess.run(
        [sys.executable, "-m", RUNNER, "--help"],
        capture_output=True,
        text=True,
        timeout=120,
    )
    assert result.returncode == 0
    for flag in ("--opponent-group", "--game-id", "--status"):
        assert flag in result.stdout


@pytest.mark.parametrize(
    ("missing", "extra"),
    [
        ("--opponent-group", ["--game-id", "NC-X", "--status", "s.json"]),
        ("--game-id", ["--opponent-group", "GRPX", "--status", "s.json"]),
        ("--status", ["--opponent-group", "GRPX", "--game-id", "NC-X"]),
    ],
)
def test_remote_series_requires_every_new_match_argument(missing, extra, tmp_path):
    result = _run(*extra)
    assert result.returncode != 0
    assert f"{missing} is required with --opponent" in result.stderr


def test_status_no_longer_falls_back_to_a_fixed_default():
    result = _run("--opponent-group", "GRPX", "--game-id", "NC-X")
    assert result.returncode != 0
    assert "--status is required with --opponent" in result.stderr


@pytest.mark.parametrize(
    ("flag", "value"),
    [
        ("--opponent-group", "bad group"),
        ("--opponent-group", "bad/group"),
        ("--game-id", "bad id"),
        ("--game-id", "../escape"),
    ],
)
def test_unsafe_group_or_game_id_is_rejected(flag, value, tmp_path):
    args = {"--opponent-group": "GRPX", "--game-id": "NC-X"}
    args[flag] = value
    status = tmp_path / "new-series.json"
    result = _run(*sum(([k, v] for k, v in args.items()), []), "--status", str(status))
    assert result.returncode != 0
    assert f"{flag} must match" in result.stderr
    assert not status.exists()


def test_existing_status_path_is_refused(tmp_path):
    status = tmp_path / "already-there.json"
    status.write_text("{}", encoding="utf-8")
    result = _run(
        "--opponent-group", "GRPX", "--game-id", "NC-X", "--status", str(status)
    )
    assert result.returncode != 0
    assert "--status already exists" in result.stderr
    assert status.read_text(encoding="utf-8") == "{}"


def test_existing_counted_result_is_refused(tmp_path):
    counted = tmp_path / "counted"
    counted.mkdir()
    (counted / "result_NC-X.json").write_text("{}", encoding="utf-8")
    result = _run(
        "--opponent-group", "GRPX",
        "--game-id", "NC-X",
        "--status", str(tmp_path / "new.json"),
        "--counted-result-dir", str(counted),
        "--public-mcp-url", "https://salareen.example/mcp",
    )
    assert result.returncode != 0
    assert "counted result already exists" in result.stderr
