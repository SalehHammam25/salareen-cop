"""Runtime plugin fallback tests."""

import importlib

import pytest

from salareen_cop.base_logic.state_types import Coordinate
from salareen_cop.strategy.gateway import StrategyGateway
from salareen_cop.strategy.results import PluginError, ValidatedDecision
from salareen_cop.strategy.selector import select_strategy


def selection(tmp_path, monkeypatch, name, method):
    source = (
        "from salareen_cop.base_logic.actions import MoveAction, MoveChoice\n"
        "from salareen_cop.base_logic.state_types import Coordinate, Role\n"
        "from salareen_cop.strategy.results import ProposedAction\n"
        f"class Plugin:\n{method}\n"
    )
    (tmp_path / f"{name}.py").write_text(source, encoding="utf-8")
    monkeypatch.syspath_prepend(str(tmp_path))
    importlib.invalidate_caches()
    private = tmp_path / f"{name}.toml"
    private.write_text(
        f'[strategy]\npolice_class = "{name}:Plugin"\n', encoding="utf-8"
    )
    return select_strategy(private)


@pytest.mark.parametrize(
    ("name", "method", "error"),
    [
        (
            "raising_cop_plugin",
            "    def propose(self, snapshot):\n"
            "        raise RuntimeError('secret-value')",
            PluginError.RUNTIME_EXCEPTION,
        ),
        (
            "malformed_cop_plugin",
            "    def propose(self, snapshot):\n        return object()",
            PluginError.INVALID_RESULT,
        ),
        (
            "wrong_role_cop_plugin",
            "    def propose(self, snapshot):\n"
            "        return ProposedAction(MoveAction(Role.THIEF, "
            "MoveChoice.STAY), 0)",
            PluginError.PROPOSAL_REJECTED,
        ),
        (
            "illegal_cop_plugin",
            "    def propose(self, snapshot):\n"
            "        return ProposedAction(MoveAction(Role.COP, MoveChoice.SOUTH, "
            "Coordinate(2, 2)), 0)",
            PluginError.PROPOSAL_REJECTED,
        ),
    ],
)
def test_plugin_failure_uses_visible_validated_fallback(
    tmp_path, monkeypatch, rules, initial_game, name, method, error
) -> None:
    selected = selection(tmp_path, monkeypatch, name, method)
    result = StrategyGateway(rules, selected.policy).decide(
        initial_game, Coordinate(2, 2)
    )
    assert isinstance(result, ValidatedDecision)
    assert result.action.role == "cop"
    assert result.fallback_reason.error is error
    assert "secret-value" not in str(result.fallback_reason)
    assert initial_game.positions.cop == Coordinate(0, 0)


def test_fallback_is_repeatable(tmp_path, monkeypatch, rules, initial_game) -> None:
    selected = selection(
        tmp_path, monkeypatch, "repeat_cop_plugin",
        "    def propose(self, snapshot):\n        raise ValueError('private')",
    )
    gateway = StrategyGateway(rules, selected.policy)
    first = gateway.decide(initial_game, Coordinate(2, 2))
    second = gateway.decide(initial_game, Coordinate(2, 2))
    assert first == second
