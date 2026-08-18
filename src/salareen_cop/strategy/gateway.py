"""Revalidate every cop strategy proposal through Base Logic."""

from typing import Protocol

from salareen_cop.base_logic.action_results import ActionAccepted
from salareen_cop.base_logic.actions import BarrierAction, MoveAction
from salareen_cop.base_logic.rules import BaseLogicRules
from salareen_cop.base_logic.state_types import Coordinate, GameState, Role

from .models import StrategySnapshot, snapshot_for
from .results import (
    DecisionError,
    DecisionFailure,
    DecisionResult,
    FallbackReason,
    PluginError,
    ProposalResult,
    ProposedAction,
    ValidatedDecision,
)


class CopPolicy(Protocol):
    def propose(self, snapshot: StrategySnapshot) -> ProposalResult: ...


class StrategyGateway:
    def __init__(self, rules: BaseLogicRules, policy: CopPolicy) -> None:
        self._rules = rules
        self._policy = policy

    def decide(self, state: GameState, target: Coordinate) -> DecisionResult:
        snapshot = snapshot_for(state, target)
        try:
            proposal = self._policy.propose(snapshot)
        except Exception as error:
            return DecisionFailure(DecisionError.POLICY_EXCEPTION, type(error).__name__)
        if isinstance(proposal, DecisionFailure):
            return proposal
        if not isinstance(proposal, ProposedAction):
            return self._fallback(state, snapshot, PluginError.INVALID_RESULT)
        return self._validate(state, snapshot, proposal, allow_fallback=True)

    def _validate(
        self,
        state: GameState,
        snapshot: StrategySnapshot,
        proposal: ProposedAction,
        *,
        allow_fallback: bool,
    ) -> DecisionResult:
        action = proposal.action
        valid = isinstance(action, (MoveAction, BarrierAction))
        valid = valid and action.role is Role.COP
        if not valid:
            return self._reject_or_fallback(
                state, snapshot, PluginError.PROPOSAL_REJECTED, allow_fallback
            )
        validated = self._rules.apply(state, action)
        if not isinstance(validated, ActionAccepted):
            return self._reject_or_fallback(
                state, snapshot, PluginError.PROPOSAL_REJECTED, allow_fallback
            )
        return ValidatedDecision(action, validated.state, proposal.fallback_reason)

    def _reject_or_fallback(
        self,
        state: GameState,
        snapshot: StrategySnapshot,
        error: PluginError,
        allow_fallback: bool,
    ) -> DecisionResult:
        if allow_fallback and callable(getattr(self._policy, "fallback", None)):
            return self._fallback(state, snapshot, error)
        return DecisionFailure(DecisionError.ILLEGAL_PROPOSAL)

    def _fallback(
        self, state: GameState, snapshot: StrategySnapshot, error: PluginError
    ) -> DecisionResult:
        fallback = getattr(self._policy, "fallback", None)
        if not callable(fallback):
            return DecisionFailure(DecisionError.INVALID_PROPOSAL)
        proposal = fallback(snapshot, FallbackReason(error))
        if not isinstance(proposal, ProposedAction):
            return DecisionFailure(DecisionError.INVALID_PROPOSAL)
        return self._validate(state, snapshot, proposal, allow_fallback=False)
