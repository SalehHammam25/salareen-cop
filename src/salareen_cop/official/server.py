"""One stable FastMCP endpoint serving both Salareen roles."""

from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

from .mailbox import OfficialMailboxes, enqueue
from .wire import MAX_MESSAGE_BYTES, clean_audit, clean_turn


def build_unified_server(
    mailboxes: OfficialMailboxes, bearer_token: str | None = None
) -> FastMCP:
    server = FastMCP("salareen-official-reference-v1")

    def authorize() -> None:
        if bearer_token is None:
            return
        headers = get_http_headers(include_all=True)
        supplied = headers.get("authorization", headers.get("Authorization", ""))
        if supplied != f"Bearer {bearer_token}":
            raise PermissionError("invalid bearer token")

    @server.tool
    def negotiate(message: dict) -> dict:
        authorize()
        if not isinstance(message, dict):
            return {"accepted": False, "reason": "invalid_agreement"}
        result = enqueue(mailboxes.agreements, dict(message))
        offer = mailboxes.offer_for(message.get("sub_game_number"))
        return offer if result["accepted"] and offer is not None else result

    @server.tool
    def receive_turn(message: dict) -> dict:
        authorize()
        clean = clean_turn(message)
        if clean is None:
            return {"accepted": False, "reason": "invalid_turn"}
        return enqueue(mailboxes.turns, clean)

    @server.tool
    def submit_audit(payload: dict) -> dict:
        authorize()
        clean = clean_audit(payload)
        if clean is None:
            return {"accepted": False, "reason": "invalid_audit"}
        return enqueue(mailboxes.audits, clean)

    @server.tool
    def receive_control(message: dict) -> dict:
        authorize()
        if not isinstance(message, dict):
            return {"accepted": False, "reason": "invalid_control"}
        return enqueue(mailboxes.controls, dict(message))

    return server


__all__ = ["MAX_MESSAGE_BYTES", "build_unified_server"]
