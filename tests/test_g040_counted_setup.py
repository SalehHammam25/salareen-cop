"""Targeted checks for the explicit game id and the counted email format."""

import base64
import subprocess
import sys
from email import policy
from email.parser import BytesParser
from pathlib import Path

from salareen_cop.gmail_reporting import GmailReportSender, build_json_message
from salareen_cop.official.counted_email import build_counted_message
from salareen_cop.official.reporting import build_counted_result, write_counted_result
from salareen_cop.official.series import OfficialSeries
from salareen_cop.official.settlement import consensus_preimage, consensus_sha
from salareen_cop.official.terms import derive_game_ids, greeting
from tests.test_counted_reporting import PEER, POLICE_SHA, _series
from tests.test_gmail_reporting import FakeService

GAME_ID = "G040"
LECTURER = "rmisegal+uoh26finalgame@gmail.com"
SENDER = "areentarabeh1@gmail.com"


def _parsed(body: dict) -> object:
    return BytesParser(policy=policy.default).parsebytes(
        base64.urlsafe_b64decode(body["raw"])
    )


def test_explicit_game_id_reaches_negotiation_greeting():
    message = greeting("police", 1, POLICE_SHA, "amireman", None, GAME_ID)
    assert message["game_id"] == GAME_ID


def test_omitted_game_id_preserves_derived_behaviour():
    message = greeting("police", 1, POLICE_SHA, "amireman")
    assert "game_id" not in message
    assert derive_game_ids("salareen", "amireman")[0] == "amireman-vs-salareen"


def test_series_carries_the_override_and_defaults_to_none():
    series = OfficialSeries(None, None, None, {}, game_id=GAME_ID)
    assert series.game_id == GAME_ID
    assert OfficialSeries(None, None, None, {}).game_id is None


def test_game_id_enters_the_existing_consensus_input():
    rows = build_counted_result(_series(), PEER)["sub_games"]
    assert consensus_preimage(GAME_ID, rows)["game_id"] == GAME_ID
    assert consensus_sha(GAME_ID, rows) != consensus_sha("amireman-vs-salareen", rows)


def test_counted_result_filename_uses_the_official_game_id(tmp_path):
    series = _series()
    series.game_id = GAME_ID
    path = write_counted_result(tmp_path, series, PEER)
    assert path.name == "result_G040.json"


def test_counted_message_subject_body_and_attachment_are_exact():
    doc = build_counted_result(_series(), PEER)
    doc["game_id"] = GAME_ID
    message = _parsed(build_counted_message(SENDER, LECTURER, doc))
    assert message["Subject"] == "[uoh26finalgame] result report G040"
    assert message["From"] == SENDER and message["To"] == LECTURER
    assert message.get_body(("plain",)).get_content().strip() == (
        "Automated final result report for game G040. Signed JSON report attached."
    )
    attachment = next(message.iter_attachments())
    assert attachment.get_filename() == "result_G040.json"
    assert attachment.get_content_type() == "application/json"


def test_friendly_message_format_is_unchanged():
    message = _parsed(
        build_json_message(SENDER, "friend@example.test", {"verified": True})
    )
    assert message["Subject"] == "Salareen verified series report"
    assert next(message.iter_attachments()).get_filename() == "verified-series.json"


def test_default_sender_still_uses_the_friendly_builder():
    service = FakeService()
    GmailReportSender(service).send(SENDER, "friend@example.test", {"a": 1}, "k1")
    body = service.messages_api.calls[0]["body"]
    assert _parsed(body)["Subject"] == "Salareen verified series report"


def test_runner_exposes_the_game_id_flag():
    result = subprocess.run(
        [sys.executable, "-m", "salareen_cop.official.runner", "--help"],
        capture_output=True,
        text=True,
        cwd=Path.cwd(),
        timeout=60,
    )
    assert "--game-id" in result.stdout
