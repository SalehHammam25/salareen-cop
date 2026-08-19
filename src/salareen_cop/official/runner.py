"""CLI for the stable, unified Salareen official-protocol endpoint."""

import argparse
import json
import sys
import threading
import time
from dataclasses import asdict
from pathlib import Path

from salareen_cop.official.engine import CopEngine
from salareen_cop.official.mailbox import OfficialMailboxes
from salareen_cop.official.report_identity import salareen_identity
from salareen_cop.official.reporting import write_counted_result
from salareen_cop.official.series import OfficialSeries
from salareen_cop.official.server import build_unified_server
from salareen_cop.official.transport import OfficialTransport
from salareen_cop.official.wire import HEX40


def _thief_engine():
    try:
        from salareen_thief.official.engine import ThiefEngine
    except ModuleNotFoundError:
        workspace = Path(__file__).resolve().parents[4]
        sibling = workspace / "salareen-thief" / "src"
        if not sibling.is_dir():
            raise RuntimeError(
                "install the matching salareen-thief repository"
            ) from None
        sys.path.insert(0, str(sibling))
        from salareen_thief.official.engine import ThiefEngine
    return ThiefEngine


def _commit(value: str) -> str:
    if HEX40.fullmatch(value) is None:
        raise argparse.ArgumentTypeError(
            "commit must be 40 lowercase hexadecimal characters"
        )
    return value


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--opponent", help="opponent's stable https://.../mcp URL")
    parser.add_argument("--police-commit", type=_commit)
    parser.add_argument("--thief-commit", type=_commit)
    parser.add_argument("--opponent-token")
    parser.add_argument("--incoming-token")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", default=8799, type=int)
    parser.add_argument("--turn-timeout", default=180.0, type=float)
    parser.add_argument("--status", default=".runtime/official-series-result.json")
    parser.add_argument("--counted-result-dir", type=Path)
    parser.add_argument("--public-mcp-url")
    parser.add_argument("--llm-model", default="Codex GPT-5")
    args = parser.parse_args()

    mailboxes = OfficialMailboxes()
    series = None
    if args.opponent:
        if not args.police_commit or not args.thief_commit:
            parser.error(
                "--police-commit and --thief-commit are required with --opponent"
            )
        if args.counted_result_dir and not args.public_mcp_url:
            parser.error("--public-mcp-url is required with --counted-result-dir")
        transport = OfficialTransport(args.opponent, mailboxes, args.opponent_token)
        thief_engine = _thief_engine()
        commits = {"police": args.police_commit, "thief": args.thief_commit}
        identity = salareen_identity(commits, args.public_mcp_url or "", args.llm_model)

        def factory(role: str, number: int, commit: str):
            cls = CopEngine if role == "police" else thief_engine
            return cls(number, commit)

        series = OfficialSeries(
            transport,
            mailboxes,
            factory,
            commits,
            identity=identity,
        )

    def play() -> None:
        time.sleep(0.5)
        status = Path(args.status)
        status.parent.mkdir(parents=True, exist_ok=True)
        try:
            series_result = series.run(args.turn_timeout)
            payload = asdict(series_result)
            if args.counted_result_dir:
                counted_path = write_counted_result(
                    args.counted_result_dir,
                    series_result,
                    args.opponent,
                )
                payload["counted_result_path"] = str(counted_path)
        except Exception as error:
            payload = {"error": type(error).__name__, "detail": str(error)}
        status.write_text(
            json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8"
        )

    if series is not None:
        threading.Thread(target=play, daemon=True, name="official-series").start()
    server = build_unified_server(mailboxes, args.incoming_token)
    server.run(transport="http", host=args.host, port=args.port)


if __name__ == "__main__":
    main()
