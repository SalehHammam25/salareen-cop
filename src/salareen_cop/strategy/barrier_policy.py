"""Optional deterministic containment-barrier proposals."""

from salareen_cop.base_logic.actions import BarrierAction
from salareen_cop.base_logic.movement import target_for
from salareen_cop.base_logic.state_types import EpisodeStatus, Role

from .models import StrategySnapshot
from .results import DecisionError, DecisionFailure, ProposalResult, ProposedAction
from .search import distance_map
from .tie import MOVEMENT_ORDER


class ContainmentBarrierPolicy:
    """Block a target-adjacent escape cell without losing cop reachability."""

    def propose(self, snapshot: StrategySnapshot) -> ProposalResult:
        if snapshot.status is EpisodeStatus.TERMINAL:
            return DecisionFailure(DecisionError.TERMINAL_STATE)
        if snapshot.remaining_barriers <= 0:
            return DecisionFailure(DecisionError.NO_SAFE_BARRIER)
        baseline = distance_map(snapshot)
        if snapshot.cop not in baseline:
            return DecisionFailure(DecisionError.UNREACHABLE_TARGET)
        safe = []
        for order, candidate in enumerate(self._candidates(snapshot)):
            distances = distance_map(snapshot, candidate)
            if snapshot.cop in distances and self._has_exit(snapshot, candidate):
                safe.append((distances[snapshot.cop], order, candidate, len(distances)))
        if safe:
            _, _, candidate, explored = min(safe)
            return ProposedAction(BarrierAction(Role.COP, candidate), explored)
        return DecisionFailure(DecisionError.NO_SAFE_BARRIER)

    @staticmethod
    def _candidates(snapshot: StrategySnapshot):
        for choice in MOVEMENT_ORDER:
            candidate = target_for(snapshot.cop, choice)
            if (
                snapshot.board.contains(candidate)
                and candidate not in snapshot.barriers
                and candidate != snapshot.target
                and abs(candidate.row - snapshot.target.row)
                + abs(candidate.col - snapshot.target.col)
                == 1
            ):
                yield candidate

    @staticmethod
    def _has_exit(snapshot: StrategySnapshot, candidate) -> bool:
        blocked = snapshot.barriers | {candidate}
        return any(
            snapshot.board.contains(target_for(snapshot.cop, choice))
            and target_for(snapshot.cop, choice) not in blocked
            for choice in MOVEMENT_ORDER
        )
