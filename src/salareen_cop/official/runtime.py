"""One official pushed-turn mini-game with mutual audit."""

import time
from datetime import UTC, datetime

from .audit_window import LOG, await_window, sweep_backlog
from .delivery import DeliveryInbox, EquivocationError, ReorderWindowError
from .settlement import verify_records
from .terms import TERMS
from .wire import clean_turn


class SubGameRuntime:
    def __init__(self, engine, transport, sub_game: int) -> None:
        self.engine = engine
        self.transport = transport
        self.sub_game = sub_game
        self.delivery = DeliveryInbox()
        self.result: str | None = None

    def _send_turn(self, *, hold: bool = False, incoming: dict | None = None) -> None:
        message = (
            self.engine.take_turn(incoming, hold=hold)
            if hold
            else self.engine.take_turn(incoming)
        )
        self.transport.send_turn(message)
        if message.get("win_claim"):
            self.result = "survival"

    def _terminal_duplicate(self, message: dict) -> None:
        response = message.get("claim_response")
        if (
            self.engine.role == "police"
            and isinstance(response, dict)
            and response.get("caught")
        ):
            self.result = "capture"
        elif message.get("win_claim"):
            self.result = "survival"

    def _process(self, message: dict) -> None:
        outcome = self.engine.receive(message)
        if outcome.won:
            self.result = "capture"
        elif outcome.opponent_won:
            self.result = "survival"
        elif outcome.caught:
            self._send_turn(hold=True, incoming=message)
            self.result = "capture"
        else:
            self._send_turn(incoming=message)

    def run(self, turn_timeout: float = 180.0) -> dict:
        started_at = datetime.now(UTC).isoformat()
        LOG.info("subgame %s start role=%s", self.sub_game, self.engine.role)
        if self.engine.role == "thief":
            self._send_turn()
        deadline = time.monotonic() + turn_timeout
        while self.result is None:
            raw = self.transport.poll_turn(0.3)
            if raw is None:
                if time.monotonic() >= deadline:
                    self.result = "timeout"
                continue
            message = clean_turn(raw)
            if message is None:
                LOG.info("turn ignored sub_game=%s reason=malformed", self.sub_game)
                continue
            deadline = time.monotonic() + turn_timeout
            try:
                ready = self.delivery.offer(message)
            except (EquivocationError, ReorderWindowError) as error:
                LOG.info(
                    "turn rejected sub_game=%s step=%s reason=%s",
                    self.sub_game,
                    message["step"],
                    type(error).__name__,
                )
                self.result = "technical_loss"
                break
            if not ready:
                LOG.info(
                    "turn duplicate sub_game=%s step=%s",
                    self.sub_game,
                    message["step"],
                )
                self._terminal_duplicate(message)
            for item in ready:
                LOG.info(
                    "turn accepted sub_game=%s step=%s sender=%s",
                    self.sub_game,
                    item["step"],
                    item["sender"],
                )
                self._process(item)
                if self.result is not None:
                    break
            if (
                self.result is None
                and self.engine.role == "police"
                and self.engine.step >= TERMS["max_steps"]
            ):
                self.result = "survival"
        summary = self._finish(min(turn_timeout, 30.0))
        summary.update(
            {
                "started_at": started_at,
                "ended_at": datetime.now(UTC).isoformat(),
                "steps": self.engine.step,
                "tokens_total": 0,
                "peer_tokens_total": 0,
            }
        )
        return summary

    def _finish(self, audit_wait: float) -> dict:
        envelope = {
            "sender": self.engine.role,
            "records": self.engine.records,
            "result_claim": self.result,
            "sub_game": self.sub_game,
            "sub_game_number": self.sub_game,
        }
        early = sweep_backlog(self.transport, self.sub_game)
        self.transport.send_audit(envelope)
        if early is None:
            early = await_window(self.transport, self.sub_game, audit_wait)
        peer = early
        verified = bool(peer) and verify_records(peer["records"], self.delivery.played)
        agreed = bool(peer) and peer["result_claim"] == self.result
        return {
            "sub_game_number": self.sub_game,
            "role": self.engine.role,
            "result": self.result,
            "audit": {
                "log_verified": verified,
                "tampered": bool(peer) and not verified,
                "local_result_claim": self.result,
                "peer_result_claim": peer.get("result_claim") if peer else None,
                "result_agreed": agreed,
            },
        }
