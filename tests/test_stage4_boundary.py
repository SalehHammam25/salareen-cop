"""Static Stage 4 dependency and information-boundary tests."""

import ast
from dataclasses import fields
from pathlib import Path

from salareen_cop.scent.models import OpponentScent


def imports(path: Path) -> set[str]:
    tree = ast.parse(path.read_text(encoding="utf-8"))
    found = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            found.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            found.add(node.module)
    return found


def test_base_logic_has_no_stage3_or_stage4_reverse_dependency() -> None:
    forbidden = ("strategy", "scent", "belief", "language")
    violations = {
        path
        for path in Path("src/salareen_cop/base_logic").glob("*.py")
        if any(any(name in module for name in forbidden) for module in imports(path))
    }
    assert violations == set()


def test_strategy_never_imports_language_or_provider_code() -> None:
    violations = {
        (path, module)
        for path in Path("src/salareen_cop/strategy").glob("*.py")
        for module in imports(path)
        if "language" in module or "provider" in module
    }
    assert violations == set()


def test_stage4_has_no_future_stage_or_network_imports() -> None:
    forbidden = ("ngrok", "crypto", "gui", "report", "fastmcp", "mcp_transport")
    roots = ("scent", "belief", "language")
    violations = {
        (path, module)
        for root in roots
        for path in Path(f"src/salareen_cop/{root}").glob("*.py")
        for module in imports(path)
        if any(name in module for name in forbidden)
    }
    assert violations == set()


def test_language_does_not_import_base_logic_or_strategy() -> None:
    violations = {
        (path, module)
        for path in Path("src/salareen_cop/language").glob("*.py")
        for module in imports(path)
        if "base_logic" in module or "strategy" in module
    }
    assert violations == set()


def test_opponent_scent_exposes_no_source_position_or_action() -> None:
    assert {item.name for item in fields(OpponentScent)} == {"turn", "grid"}
