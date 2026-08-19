"""One official pushed-turn mini-game with mutual audit."""

import time

from .delivery import DeliveryInbox, EquivocationError, ReorderWindowError
from .settlement import verify_records
from .terms import TERMS
from .wire import clean_audit, clean_turn


class SubGameRuntime:
    def __init__(self, engine, transport, sub_game: int) -> None:
        self.engine = engine
        self.transport = transport
        self.sub_game = sub_game
        self.delivery = DeliveryInbox()
        self.result: str | None = None

    def _send_turn(self, *, hold: bool = False, incoming: dict | None = None) -> None:
        message = self.engine.take_turn(incoming, hold=hold) if hold else self.engine.take_turn(incoming)
        self.transport.send_turn(message)
        if message.get("win_claim"):
            self.result = "survival"

    def _terminal_duplicate(self, message: dict) -> None:
        response = message.get("claim_response")
        if self.engine.role == "police" and isinstance(response, dict) and response.get("caught"):
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
                continue
            deadline = time.monotonic() + turn_timeout
            try:
                ready = self.delivery.offer(message)
            except (EquivocationError, ReorderWindowError):
                self.result = "technical_loss"
                break
            if not ready:
                self._terminal_duplicate(message)
            for item in ready:
                self._process(item)
                if self.result is not None:
                    break
            if (
                self.result is None
                and self.engine.role == "police"
                and self.engine.step >= TERMS["max_steps"]
            ):
                self.result = "survival"
        return self._finish(min(turn_timeout, 30.0))

    def _finish(self, audit_wait: float) -> dict:
        envelope = {
            "sender": self.engine.role,
            "records": self.engine.records,
            "result_claim": self.result,
        }
        self.transport.send_audit(envelope)
        peer = None
        deadline = time.monotonic() + audit_wait
        while time.monotonic() < deadline:
            raw = self.transport.poll_audit(deadline - time.monotonic())
            if raw is None:
                break
            candidate = clean_audit(raw)
            if candidate and candidate.get("consensus_sha") is None:
                peer = candidate
                break
        verified = bool(peer) and verify_records(peer["records"], self.delivery.played)
        agreed = bool(peer) and peer["result_claim"] == self.result
        while self.transport.poll_turn(0.0) is not None:
            pass
        return {
            "sub_game_number": self.sub_game,
            "role": self.engine.role,
            "result": self.result,
            "audit": {"log_verified": verified, "result_agreed": agreed},
        }
