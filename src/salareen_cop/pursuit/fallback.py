"""The previous greedy scent-chasing police policy, retained as a fallback."""

from salareen_cop.base_logic.actions import MoveAction
from salareen_cop.base_logic.state_types import Board, Coordinate, EpisodeStatus
from salareen_cop.strategy.blind import BlindCopPolicy
from salareen_cop.strategy.models import StrategySnapshot
from salareen_cop.strategy.results import ProposedAction


def greedy_choice(
    board: Board,
    position: Coordinate,
    barriers: frozenset[Coordinate],
    remaining_barriers: int,
    target: Coordinate,
) -> str:
    """Return the legacy blind shortest-path move toward one stale cell."""
    snapshot = StrategySnapshot(
        board,
        position,
        barriers,
        remaining_barriers,
        EpisodeStatus.ACTIVE,
        target,
    )
    proposal = BlindCopPolicy().propose(snapshot)
    if not isinstance(proposal, ProposedAction):
        return "STAY"
    if not isinstance(proposal.action, MoveAction):
        return "STAY"
    return proposal.action.choice.value
