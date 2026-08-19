"""Official wire engine backed by Salareen's existing Cop policy."""

import secrets
from dataclasses import dataclass
from datetime import UTC, datetime

from salareen_cop.base_logic.actions import MoveAction
from salareen_cop.base_logic.state_types import Board, Coordinate, EpisodeStatus
from salareen_cop.strategy.blind import BlindCopPolicy
from salareen_cop.strategy.models import StrategySnapshot
from salareen_cop.strategy.results import ProposedAction

from .terms import TERMS, commit_of

DELTAS = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "W": (0, -1), "STAY": (0, 0)}


@dataclass(frozen=True)
class IncomingOutcome:
    won: bool = False
    caught: bool = False
    opponent_won: bool = False


class CopEngine:
    role = "police"

    def __init__(self, sub_game: int, git_commit: str) -> None:
        self.sub_game = sub_game
        self.git_commit = git_commit
        self.board = Board(7, 0, "top-left")
        self.position = Coordinate(*TERMS["cop_start"])
        self.barriers: set[Coordinate] = set()
        self.policy = BlindCopPolicy()
        self.step = 0
        self.records: list[dict] = []
        self._record("STAY", "initial", None, None)

    def _target(self, scent: dict) -> Coordinate:
        if not scent:
            return Coordinate(*TERMS["thief_start"])
        key = max(scent, key=lambda item: (scent[item], item))
        row, col = (int(part) for part in key.split(","))
        return Coordinate(row, col)

    def _choice(self, scent: dict) -> str:
        snapshot = StrategySnapshot(
            self.board,
            self.position,
            frozenset(self.barriers),
            TERMS["barriers_max"] - len(self.barriers),
            EpisodeStatus.ACTIVE,
            self._target(scent),
        )
        proposal = self.policy.propose(snapshot)
        if not isinstance(proposal, ProposedAction) or not isinstance(
            proposal.action, MoveAction
        ):
            return "STAY"
        return proposal.action.choice.value

    def _apply_move(self, choice: str) -> None:
        row, col = DELTAS.get(choice, (0, 0))
        target = Coordinate(self.position.row + row, self.position.col + col)
        if self.board.contains(target) and target not in self.barriers:
            self.position = target

    def _scent(self) -> dict[str, float]:
        rings = (0.9, 0.6, 0.3)
        result = {}
        for row in range(7):
            for col in range(7):
                distance = max(abs(row - self.position.row), abs(col - self.position.col))
                if distance < len(rings):
                    result[f"{row},{col}"] = rings[distance]
        return result

    def _record(
        self,
        move: str,
        intent: str,
        response: dict | None,
        capture_claim: list[int] | None,
    ) -> dict:
        payload = {
            "capture_claim": capture_claim,
            "claim_response": response,
            "hint": "",
            "intent": intent,
            "move": move,
            "position": [self.position.row, self.position.col],
            "role": self.role,
            "state": "ok",
            "step": self.step,
            "sub_game": self.sub_game,
        }
        nonce = secrets.token_hex(16)
        record = {"payload": payload, "nonce": nonce, "commit": commit_of(payload, nonce)}
        self.records.append(record)
        return record

    def receive(self, message: dict) -> IncomingOutcome:
        barrier = message.get("barrier_placed")
        if barrier is not None:
            self.barriers.add(Coordinate(*barrier))
        response = message.get("claim_response")
        won = isinstance(response, dict) and response.get("caught") is True
        opponent_won = bool(message.get("win_claim"))
        return IncomingOutcome(won=won, opponent_won=opponent_won)

    def take_turn(self, incoming: dict | None = None) -> dict:
        self.step += 1
        choice = self._choice((incoming or {}).get("smell_grid", {}))
        self._apply_move(choice)
        claim = [self.position.row, self.position.col]
        record = self._record(
            "STAY" if choice == "STAY" else f"MOVE:{choice}",
            "pursue scent belief",
            None,
            claim,
        )
        return {
            "step": self.step,
            "sender": self.role,
            "commit": record["commit"],
            "hint": "",
            "smell_grid": self._scent(),
            "timestamp": datetime.now(UTC).isoformat(),
            "barrier_placed": None,
            "capture_claim": claim,
            "claim_response": None,
            "win_claim": None,
        }
