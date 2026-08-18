"""Cop-specific deterministic containment barrier tests."""

from salareen_cop.base_logic.state_factory import build_state
from salareen_cop.base_logic.state_results import StateAccepted
from salareen_cop.base_logic.state_types import Coordinate
from salareen_cop.strategy.barrier_policy import ContainmentBarrierPolicy
from salareen_cop.strategy.gateway import StrategyGateway
from salareen_cop.strategy.models import snapshot_for
from salareen_cop.strategy.results import (
    DecisionError,
    DecisionFailure,
    ProposedAction,
    ValidatedDecision,
)


def state_with(config, *, cop, thief, barriers=(), usage=None):
    usage = len(tuple(barriers)) if usage is None else usage
    result = build_state(
        config, thief=thief, cop=cop, barriers=barriers, barrier_usage=usage
    )
    assert isinstance(result, StateAccepted)
    return result.value


def test_legal_containment_barrier_is_validated(accepted_config, rules) -> None:
    state = state_with(accepted_config, cop=Coordinate(3, 3), thief=Coordinate(6, 6))
    target = Coordinate(2, 4)
    result = StrategyGateway(rules, ContainmentBarrierPolicy()).decide(state, target)
    assert isinstance(result, ValidatedDecision)
    assert result.action.target == Coordinate(2, 3)
    assert result.action.target in result.state.barriers
    assert state.barriers == frozenset()


def test_barrier_tie_order_is_repeatable(accepted_config) -> None:
    state = state_with(accepted_config, cop=Coordinate(3, 3), thief=Coordinate(6, 6))
    snapshot = snapshot_for(state, Coordinate(2, 4))
    first = ContainmentBarrierPolicy().propose(snapshot)
    assert isinstance(first, ProposedAction)
    assert first == ContainmentBarrierPolicy().propose(snapshot)


def test_quota_and_no_candidate_are_explicit(accepted_config) -> None:
    state = state_with(
        accepted_config,
        cop=Coordinate(0, 0),
        thief=Coordinate(6, 6),
        usage=accepted_config.movement.max_barriers,
    )
    result = ContainmentBarrierPolicy().propose(snapshot_for(state, Coordinate(2, 2)))
    assert result == DecisionFailure(DecisionError.NO_SAFE_BARRIER)


def test_existing_and_off_board_candidates_are_never_proposed(
    accepted_config,
) -> None:
    state = state_with(
        accepted_config,
        cop=Coordinate(0, 0),
        thief=Coordinate(6, 6),
        barriers=(Coordinate(0, 1),),
    )
    result = ContainmentBarrierPolicy().propose(snapshot_for(state, Coordinate(1, 1)))
    assert isinstance(result, DecisionFailure)


def test_self_containing_candidate_is_refused(accepted_config) -> None:
    barriers = (Coordinate(1, 0), Coordinate(0, 1))
    state = state_with(
        accepted_config,
        cop=Coordinate(0, 0),
        thief=Coordinate(6, 6),
        barriers=barriers,
    )
    result = ContainmentBarrierPolicy().propose(snapshot_for(state, Coordinate(1, 1)))
    assert result == DecisionFailure(DecisionError.UNREACHABLE_TARGET)


def test_hidden_true_thief_collision_cannot_bypass_rules(
    accepted_config, rules
) -> None:
    state = state_with(accepted_config, cop=Coordinate(3, 3), thief=Coordinate(2, 3))
    before = state
    result = StrategyGateway(rules, ContainmentBarrierPolicy()).decide(
        state, Coordinate(2, 4)
    )
    assert isinstance(result, DecisionFailure)
    assert result.error is DecisionError.ILLEGAL_PROPOSAL
    assert state is before
