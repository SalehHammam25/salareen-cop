"""Wait for a clean counted series result and email it to the league recipient.

Counted-only path. The friendly (non-counted) report keeps its own separate
script and its own recipient; nothing here touches it.
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

from salareen_cop.official.counted_email import send_counted_gmail_report
from salareen_cop.official.report_validation import validate_counted_result

RECIPIENT = "rmisegal+uoh26finalgame@gmail.com"


class CountedSendSuppressed(RuntimeError):
    """Raised when a counted artifact exists but must never be emailed."""


def eligible_result(path: Path, not_before: float) -> dict | None:
    """Return the counted document only when it is clean, complete and fresh."""
    if not path.is_file():
        return None
    if path.stat().st_mtime < not_before:
        return None
    try:
        doc = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return None
    if not isinstance(doc, dict):
        return None
    if "error" in doc:
        raise CountedSendSuppressed(
            f"counted series failed; email suppressed: {doc['error']}"
        )
    try:
        validate_counted_result(doc)
    except ValueError as error:
        raise CountedSendSuppressed(
            f"counted result invalid; email suppressed: {error}"
        ) from error
    agreement = doc["mutual_agreement"]
    if not agreement.get("confirmed"):
        raise CountedSendSuppressed(
            "counted mutual agreement not confirmed; email suppressed"
        )
    if not agreement.get("results_agreed"):
        raise CountedSendSuppressed(
            "counted per-game results disputed; email suppressed"
        )
    if not agreement.get("sha_match"):
        raise CountedSendSuppressed("counted consensus SHA mismatch; email suppressed")
    return doc


def idempotency_key(doc: dict) -> str:
    """Derive one stable key per counted series settlement."""
    return f"counted:{doc['game_id']}:{doc['mutual_agreement']['sha256']}"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", type=Path, required=True)
    parser.add_argument(
        "--sender",
        required=True,
        help="authenticated Gmail account used as the From address",
    )
    parser.add_argument("--oauth-client", type=Path, required=True)
    parser.add_argument("--oauth-token", type=Path, required=True)
    parser.add_argument("--timeout", type=float, default=21600.0)
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args()
    if not args.oauth_client.is_file():
        raise FileNotFoundError(f"OAuth client JSON not found: {args.oauth_client}")

    not_before = time.time()
    deadline = time.monotonic() + args.timeout
    doc = None
    while time.monotonic() < deadline:
        doc = eligible_result(args.result, not_before)
        if doc is not None:
            break
        time.sleep(2.0)
    if doc is None:
        raise TimeoutError("counted result did not complete before email timeout")

    os.environ["SALAREEN_GMAIL_ADDRESS"] = args.sender
    os.environ["SALAREEN_GOOGLE_OAUTH_CLIENT_PATH"] = str(args.oauth_client.resolve())
    os.environ["SALAREEN_GOOGLE_OAUTH_TOKEN_PATH"] = str(args.oauth_token.resolve())
    response = send_counted_gmail_report(RECIPIENT, doc, idempotency_key(doc))
    payload = {"recipient": RECIPIENT, "gmail_response": response}
    print(json.dumps(payload, sort_keys=True))


if __name__ == "__main__":
    main()
