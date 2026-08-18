"""Deterministic blind cop pursuit policy."""

from collections.abc import Callable

from salareen_cop.base_logic.actions import MoveAction, MoveChoice
from salareen_cop.base_logic.state_types import EpisodeStatus, Role

from .models import StrategySnapshot
from .results import DecisionError, DecisionFailure, ProposalResult, ProposedAction
from .search import distance_map, shortest_choices
from .tie import configured_order_tie

TiePolicy = Callable[[tuple[MoveChoice, ...]], MoveChoice]


class BlindCopPolicy:
    def __init__(self, tie_policy: TiePolicy = configured_order_tie) -> None:
        self._tie_policy = tie_policy

    def propose(self, snapshot: StrategySnapshot) -> ProposalResult:
        if snapshot.status is EpisodeStatus.TERMINAL:
            return DecisionFailure(DecisionError.TERMINAL_STATE)
        if (
            not snapshot.board.contains(snapshot.target)
            or snapshot.target in snapshot.barriers
        ):
            return DecisionFailure(DecisionError.INVALID_TARGET)
        if snapshot.cop == snapshot.target:
            return ProposedAction(
                MoveAction(Role.COP, MoveChoice.STAY, snapshot.cop), 1
            )
        distances = distance_map(snapshot)
        choices = shortest_choices(snapshot, distances)
        if not choices:
            return DecisionFailure(DecisionError.UNREACHABLE_TARGET)
        chosen = self._tie_policy(choices)
        if chosen not in choices:
            return DecisionFailure(DecisionError.INVALID_TIE_CHOICE)
        return ProposedAction(MoveAction(Role.COP, chosen), len(distances))
