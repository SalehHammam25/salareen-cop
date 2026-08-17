"""Trusted private-TOML cop strategy selection."""

import importlib
import re
import tomllib
from dataclasses import dataclass
from pathlib import Path

from .blind import BlindCopPolicy
from .fallback import FallbackPolicy
from .results import FallbackReason, PluginError

DEFAULT_CLASS_PATH = "salareen_cop.strategy.blind:BlindCopPolicy"
_REFERENCE = re.compile(r"^[A-Za-z_]\w*(?:\.[A-Za-z_]\w*)*:[A-Za-z_]\w*$")


@dataclass(frozen=True, slots=True)
class StrategySelection:
    policy: FallbackPolicy
    configured_reference: str | None
    fallback_reason: FallbackReason | None


def _fallback(reason: FallbackReason) -> StrategySelection:
    default = BlindCopPolicy()
    return StrategySelection(FallbackPolicy(default, default, reason), None, reason)


def _load(reference: object):
    if type(reference) is not str or not _REFERENCE.fullmatch(reference):
        return None, FallbackReason(PluginError.MALFORMED_REFERENCE)
    module_name, class_name = reference.split(":", 1)
    try:
        module = importlib.import_module(module_name)
    except ModuleNotFoundError as error:
        code = (
            PluginError.MODULE_NOT_FOUND
            if error.name == module_name or module_name.startswith(f"{error.name}.")
            else PluginError.IMPORT_FAILED
        )
        return None, FallbackReason(code, type(error).__name__)
    except Exception as error:
        return None, FallbackReason(PluginError.IMPORT_FAILED, type(error).__name__)
    candidate = getattr(module, class_name, None)
    if candidate is None:
        return None, FallbackReason(PluginError.CLASS_NOT_FOUND)
    if not isinstance(candidate, type):
        return None, FallbackReason(PluginError.INVALID_INTERFACE)
    try:
        instance = candidate()
    except Exception as error:
        return None, FallbackReason(PluginError.CONSTRUCTOR_FAILED, type(error).__name__)
    if not callable(getattr(instance, "propose", None)):
        return None, FallbackReason(PluginError.INVALID_INTERFACE)
    return instance, None


def select_strategy(private_path: Path) -> StrategySelection:
    default = BlindCopPolicy()
    try:
        private = tomllib.loads(private_path.read_text(encoding="utf-8"))
    except OSError as error:
        return _fallback(
            FallbackReason(PluginError.CONFIG_READ_ERROR, type(error).__name__)
        )
    except tomllib.TOMLDecodeError:
        return _fallback(FallbackReason(PluginError.TOML_ERROR))
    section = private.get("strategy") if type(private) is dict else None
    if section is None:
        return StrategySelection(FallbackPolicy(default, default), None, None)
    if type(section) is not dict:
        return _fallback(FallbackReason(PluginError.INVALID_INTERFACE))
    reference = section.get("police_class")
    if reference is None:
        return StrategySelection(FallbackPolicy(default, default), None, None)
    plugin, reason = _load(reference)
    if reason is not None:
        return _fallback(reason)
    return StrategySelection(FallbackPolicy(plugin, default), reference, None)
