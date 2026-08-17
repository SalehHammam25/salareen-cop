"""Narrow belief target adapter into the Stage 3 gateway."""

from dataclasses import dataclass

from salareen_cop.base_logic.state_types import GameState
from salareen_cop.strategy.gateway import StrategyGateway
from salareen_cop.strategy.results import DecisionResult

from .models import BeliefMap
from .target import select_target


@dataclass(frozen=True, slots=True)
class BeliefStrategyAdapter:
    gateway: StrategyGateway

    def decide(self, state: GameState, belief: BeliefMap) -> DecisionResult:
        """Supply a target only; Stage 3 proposes and Stage 1 validates."""
        return self.gateway.decide(state, select_target(belief))
