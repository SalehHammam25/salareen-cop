"""Counted-only Gmail delivery with the league's required message format.

The non-counted friendly report keeps `build_json_message` and its own
recipient; nothing in this module is reachable from that path.
"""

import base64
import json
import os
from email.message import EmailMessage
from pathlib import Path
from typing import Any

from salareen_cop.gmail_reporting import GmailReportSender, load_gmail_service

SUBJECT_PREFIX = "[uoh26finalgame] result report"


def counted_subject(game_id: str) -> str:
    """Return the exact subject line required for a counted report."""
    return f"{SUBJECT_PREFIX} {game_id}"


def counted_body(game_id: str) -> str:
    """Return the exact body text required for a counted report."""
    return (
        f"Automated final result report for game {game_id}. "
        "Signed JSON report attached."
    )


def counted_attachment_name(game_id: str) -> str:
    """Return the singular result_<game_id>.json attachment filename."""
    return f"result_{game_id}.json"


def build_counted_message(
    sender: str, recipient: str, artifact: dict[str, Any]
) -> dict[str, str]:
    """Create the base64url MIME payload for one counted result report."""
    game_id = artifact["game_id"]
    message = EmailMessage()
    message["Subject"] = counted_subject(game_id)
    message["From"] = sender
    message["To"] = recipient
    message.set_content(counted_body(game_id))
    payload = json.dumps(artifact, sort_keys=True, indent=2).encode("utf-8")
    message.add_attachment(
        payload,
        maintype="application",
        subtype="json",
        filename=counted_attachment_name(game_id),
    )
    return {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode("ascii")}


def send_counted_gmail_report(
    recipient: str,
    artifact: dict[str, Any],
    idempotency_key: str,
) -> dict[str, Any]:
    """Send one counted report using OAuth material from path variables."""
    sender = os.environ.get("SALAREEN_GMAIL_ADDRESS")
    client_value = os.environ.get("SALAREEN_GOOGLE_OAUTH_CLIENT_PATH")
    token_value = os.environ.get("SALAREEN_GOOGLE_OAUTH_TOKEN_PATH")
    if not sender or not client_value or not token_value:
        raise RuntimeError("Gmail address and OAuth paths must be supplied")
    service = load_gmail_service(Path(client_value), Path(token_value))
    sender_client = GmailReportSender(service, message_builder=build_counted_message)
    return sender_client.send(sender, recipient, artifact, idempotency_key)
