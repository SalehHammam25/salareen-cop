"""Synchronous pushed-message client for the opponent's fixed MCP URL."""

import asyncio
import contextlib
import json
import queue
import time

from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

from .mailbox import OfficialMailboxes


def _structured(result: object) -> dict | None:
    for name in ("data", "structured_content"):
        value = getattr(result, name, None)
        if isinstance(value, dict):
            return value
    content = getattr(result, "content", None)
    if isinstance(content, list) and content:
        text = getattr(content[0], "text", None)
        if isinstance(text, str):
            with contextlib.suppress(ValueError):
                value = json.loads(text)
                return value if isinstance(value, dict) else None
    return None


class OfficialTransport:
    def __init__(
        self,
        opponent_url: str,
        mailboxes: OfficialMailboxes,
        bearer_token: str | None = None,
        connect_deadline: float = 60.0,
    ) -> None:
        self.url = opponent_url
        self.mailboxes = mailboxes
        self.headers = {}
        if bearer_token:
            self.headers["Authorization"] = f"Bearer {bearer_token}"
        self.connect_deadline = connect_deadline

    def _call_once(self, tool: str, argument: dict) -> dict | None:
        key = "payload" if tool == "submit_audit" else "message"

        async def invoke():
            transport = StreamableHttpTransport(self.url, headers=self.headers)
            async with Client(transport) as client:
                return await client.call_tool(tool, {key: argument})

        return _structured(asyncio.run(invoke()))

    def call(self, tool: str, argument: dict, timeout: float | None = None) -> dict | None:
        deadline = time.monotonic() + (self.connect_deadline if timeout is None else timeout)
        while True:
            try:
                return self._call_once(tool, argument)
            except Exception as exc:
                if time.monotonic() >= deadline:
                    raise ConnectionError(f"opponent MCP unavailable: {exc}") from exc
                time.sleep(1.0)

    def exchange_agreement(self, offer: dict, timeout: float = 300.0) -> dict:
        deadline = time.monotonic() + timeout
        wanted = offer["sub_game_number"]
        while time.monotonic() < deadline:
            reply = self.call("negotiate", offer, timeout=min(15.0, timeout))
            if isinstance(reply, dict) and isinstance(reply.get("terms"), dict):
                if reply.get("sub_game_number") in (None, wanted):
                    self.call("negotiate", offer, timeout=15.0)
                    return reply
            try:
                pushed = self.mailboxes.agreements.get(timeout=3.0)
            except queue.Empty:
                continue
            if pushed.get("sub_game_number") not in (None, wanted):
                continue
            self.call("negotiate", offer, timeout=15.0)
            return pushed
        raise TimeoutError("opponent did not complete fresh negotiation")

    def send_turn(self, message: dict) -> None:
        self.call("receive_turn", message)

    def poll_turn(self, timeout: float) -> dict | None:
        try:
            return self.mailboxes.turns.get(timeout=timeout)
        except queue.Empty:
            return None

    def send_audit(self, payload: dict) -> None:
        with contextlib.suppress(ConnectionError):
            self.call("submit_audit", payload, timeout=10.0)

    def poll_audit(self, timeout: float) -> dict | None:
        try:
            return self.mailboxes.audits.get(timeout=timeout)
        except queue.Empty:
            return None

    def send_control(self, message: dict) -> None:
        with contextlib.suppress(ConnectionError):
            self.call("receive_control", message, timeout=2.0)
