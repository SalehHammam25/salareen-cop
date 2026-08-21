"""Six-game role-alternating series and final consensus exchange."""

import re
import time
from collections.abc import Callable
from dataclasses import dataclass, field
from datetime import UTC, datetime

from .runtime import SubGameRuntime
from .settlement import consensus_row, consensus_sha
from .terms import GROUP_ID, derive_game_ids, greeting
from .wire import HEX40, clean_audit, verify_greeting

SAFE_ID = re.compile(r"^[A-Za-z0-9._-]+$")


@dataclass
class SeriesResult:
    summaries: list[dict] = field(default_factory=list)
    game_id: str = ""
    game_uid: str = ""
    consensus_sha: str = ""
    peer_consensus_sha: str | None = None
    consensus_agreed: bool = False
    game_started_at: str = ""
    game_ended_at: str = ""
    own_identity: dict = field(default_factory=dict)
    peer_identity: dict = field(default_factory=dict)


def _peer_commit(message: dict) -> str:
    identity = (
        message.get("identity") if isinstance(message.get("identity"), dict) else {}
    )
    for source in (identity, message):
        for key in ("github_commit", "git_commit_hash", "commit_hash"):
            value = source.get(key)
            if isinstance(value, str) and HEX40.fullmatch(value):
                return value
    return ""


class OfficialSeries:
    def __init__(
        self,
        transport,
        mailboxes,
        engine_factory: Callable[[str, int, str], object],
        commits: dict[str, str],
        opponent_group: str | None = None,
        identity: dict | None = None,
        game_id: str | None = None,
    ) -> None:
        self.transport = transport
        self.mailboxes = mailboxes
        self.engine_factory = engine_factory
        self.commits = commits
        self.opponent = opponent_group
        self.identity = dict(identity or {})
        self.game_id = game_id or None

    def _require_opponent(self) -> None:
        """Reject a missing, malformed, or self-referential opponent group."""
        group = self.opponent
        if not isinstance(group, str) or SAFE_ID.fullmatch(group) is None:
            raise ValueError("opponent_group must match [A-Za-z0-9._-]+")
        if group == GROUP_ID:
            raise ValueError("opponent_group must differ from our own group id")
        if self.game_id is not None and SAFE_ID.fullmatch(self.game_id) is None:
            raise ValueError("game_id must match [A-Za-z0-9._-]+")

    def run(self, turn_timeout: float = 180.0) -> SeriesResult:
        self._require_opponent()
        result = SeriesResult(
            game_started_at=datetime.now(UTC).isoformat(),
            own_identity=dict(self.identity),
        )
        derived_id, result.game_uid = derive_game_ids(GROUP_ID, self.opponent)
        result.game_id = self.game_id or derived_id
        for number in range(1, 7):
            role = "police" if number % 2 else "thief"
            peer_role = "thief" if role == "police" else "police"
            offer = greeting(
                role,
                number,
                self.commits[role],
                self.opponent,
                self.identity,
                self.game_id,
            )
            self.mailboxes.set_offer(offer)
            peer = self.transport.exchange_agreement(offer)
            group = verify_greeting(peer, peer_role, number)
            if group != self.opponent:
                raise ValueError("opponent group changed during series")
            engine = self.engine_factory(role, number, self.commits[role])
            summary = SubGameRuntime(engine, self.transport, number).run(turn_timeout)
            peer_identity = peer.get("identity")
            if isinstance(peer_identity, dict):
                result.peer_identity.update(peer_identity)
            result.peer_identity["group_id"] = group
            summary["own_github_commit"] = self.commits[role]
            summary["peer_github_commit"] = _peer_commit(peer)
            result.summaries.append(summary)
        rows = [
            consensus_row(item, GROUP_ID, self.opponent) for item in result.summaries
        ]
        result.consensus_sha = consensus_sha(result.game_id, rows)
        envelope = {
            "sender": "thief",
            "records": [],
            "result_claim": "series_consensus",
            "consensus_sha": result.consensus_sha,
        }
        self.transport.send_audit(envelope)
        deadline = time.monotonic() + min(turn_timeout, 15.0)
        while time.monotonic() < deadline:
            peer = clean_audit(self.transport.poll_audit(deadline - time.monotonic()))
            if peer is None or peer.get("result_claim") != "series_consensus":
                continue
            result.peer_consensus_sha = peer.get("consensus_sha")
            break
        result.consensus_agreed = result.peer_consensus_sha == result.consensus_sha
        self.mailboxes.set_offer(None)
        result.game_ended_at = datetime.now(UTC).isoformat()
        return result
