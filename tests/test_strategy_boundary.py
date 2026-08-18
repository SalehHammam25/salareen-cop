"""Restricted snapshot and dependency-boundary tests."""

import ast
from dataclasses import FrozenInstanceError, fields
from pathlib import Path

import pytest

from salareen_cop.base_logic.state_types import Coordinate
from salareen_cop.strategy.models import snapshot_for


def imported(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            found.add(node.module)
    return found


def test_snapshot_is_frozen_and_restricted(initial_game) -> None:
    snapshot = snapshot_for(initial_game, Coordinate(2, 2))
    assert {item.name for item in fields(snapshot)} == {
        "board",
        "cop",
        "barriers",
        "remaining_barriers",
        "status",
        "target",
    }
    for forbidden in ("thief", "session", "phase", "scent", "belief", "language"):
        assert not hasattr(snapshot, forbidden)
    with pytest.raises(FrozenInstanceError):
        snapshot.target = Coordinate(1, 1)  # type: ignore[misc]


def test_strategy_has_no_forbidden_dependencies() -> None:
    forbidden = (
        "fastmcp", "mcp", "salareen_cop.mcp_transport", "salareen_cop.scent",
        "salareen_cop.language", "salareen_cop.belief", "random", "time",
        "socket", "httpx", "requests",
    )
    violations = {
        (path, module)
        for path in Path("src/salareen_cop/strategy").glob("*.py")
        for module in imported(path)
        if any(module == item or module.startswith(f"{item}.") for item in forbidden)
    }
    assert violations == set()


def test_base_logic_never_imports_strategy() -> None:
    violations = {
        path
        for path in Path("src/salareen_cop/base_logic").glob("*.py")
        if any("strategy" in module for module in imported(path))
    }
    assert violations == set()
