"""Private cop plugin selection tests."""

import importlib

import pytest

from salareen_cop.strategy.blind import BlindCopPolicy
from salareen_cop.strategy.results import PluginError
from salareen_cop.strategy.selector import DEFAULT_CLASS_PATH, select_strategy


def private_config(tmp_path, reference=None):
    path = tmp_path / "game.toml"
    value = "" if reference is None else f'police_class = "{reference}"\n'
    path.write_text(f"[strategy]\n{value}", encoding="utf-8")
    return path


def plugin_module(tmp_path, monkeypatch, name, body):
    (tmp_path / f"{name}.py").write_text(body, encoding="utf-8")
    monkeypatch.syspath_prepend(str(tmp_path))
    importlib.invalidate_caches()
    return name


def test_default_private_selection() -> None:
    module_name, class_name = DEFAULT_CLASS_PATH.split(":")
    policy = getattr(importlib.import_module(module_name), class_name)()
    assert isinstance(policy, BlindCopPolicy)


def test_valid_private_plugin_selection(tmp_path, monkeypatch) -> None:
    name = plugin_module(
        tmp_path,
        monkeypatch,
        "good_cop_plugin",
        "class Good:\n    def propose(self, snapshot):\n        return None\n",
    )
    selected = select_strategy(private_config(tmp_path, f"{name}:Good"))
    assert selected.configured_reference == f"{name}:Good"
    assert selected.fallback_reason is None


@pytest.mark.parametrize("reference", ["bad", "a:b:c", "a-b:Class", ":Class"])
def test_malformed_references_are_sanitized(tmp_path, reference) -> None:
    selected = select_strategy(private_config(tmp_path, reference))
    assert selected.fallback_reason.error is PluginError.MALFORMED_REFERENCE
    assert selected.configured_reference is None
    assert reference not in str(selected.fallback_reason)


def test_missing_module_and_class_are_typed(tmp_path, monkeypatch) -> None:
    missing = select_strategy(private_config(tmp_path, "no_such_module:Policy"))
    assert missing.fallback_reason.error is PluginError.MODULE_NOT_FOUND
    name = plugin_module(tmp_path, monkeypatch, "empty_cop_plugin", "VALUE = 1\n")
    absent = select_strategy(private_config(tmp_path, f"{name}:Missing"))
    assert absent.fallback_reason.error is PluginError.CLASS_NOT_FOUND


@pytest.mark.parametrize(
    ("name", "body", "error"),
    [
        ("not_class", "VALUE = 1\n", PluginError.INVALID_INTERFACE),
        ("no_method", "class Bad:\n    pass\n", PluginError.INVALID_INTERFACE),
        (
            "constructor",
            "class Bad:\n    def __init__(self):\n"
            "        raise RuntimeError('private')\n",
            PluginError.CONSTRUCTOR_FAILED,
        ),
    ],
)
def test_invalid_class_or_constructor_falls_back(
    tmp_path, monkeypatch, name, body, error
) -> None:
    name = plugin_module(tmp_path, monkeypatch, f"bad_{name}", body)
    class_name = "VALUE" if body.startswith("VALUE") else "Bad"
    selected = select_strategy(private_config(tmp_path, f"{name}:{class_name}"))
    assert selected.fallback_reason.error is error
    assert "private" not in str(selected.fallback_reason)


def test_shared_json_cannot_select_plugin(tmp_path) -> None:
    shared = tmp_path / "game.json"
    shared.write_text('{"strategy":{"police_class":"remote:Bad"}}', encoding="utf-8")
    selected = select_strategy(private_config(tmp_path))
    assert selected.configured_reference is None
    assert selected.fallback_reason is None
