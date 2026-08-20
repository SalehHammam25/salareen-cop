"""Targeted checks for the counted-only lecturer email path."""

import importlib.util
import json
import time
from pathlib import Path

import pytest

from salareen_cop.official.reporting import build_counted_result
from salareen_cop.reporting import send_gmail_report
from tests.test_counted_reporting import PEER, _series

FRIENDLY_RECIPIENT = "areentarabeh1@gmail.com"
LECTURER_RECIPIENT = "rmisegal+uoh26finalgame@gmail.com"


def _module():
    path = Path("scripts/send_counted_report.py")
    spec = importlib.util.spec_from_file_location("send_counted_report", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _write(tmp_path: Path, doc: dict) -> Path:
    path = tmp_path / "result_amireman-vs-salareen.json"
    path.write_text(json.dumps(doc), encoding="utf-8")
    return path


def _clean_doc() -> dict:
    return build_counted_result(_series(), PEER)


def test_clean_counted_result_becomes_eligible(tmp_path):
    module = _module()
    path = _write(tmp_path, _clean_doc())
    doc = module.eligible_result(path, time.time() - 60)
    assert doc is not None
    assert doc["num_sub_games"] == 6 and len(doc["sub_games"]) == 6
    assert doc["mutual_agreement"]["confirmed"] is True


def test_error_artifact_suppresses_send(tmp_path):
    module = _module()
    path = _write(tmp_path, {"error": "ConnectionError", "detail": "peer down"})
    with pytest.raises(module.CountedSendSuppressed):
        module.eligible_result(path, time.time() - 60)


def test_incomplete_series_suppresses_send(tmp_path):
    module = _module()
    doc = _clean_doc()
    doc["sub_games"] = doc["sub_games"][:5]
    doc["num_sub_games"] = 5
    path = _write(tmp_path, doc)
    with pytest.raises(module.CountedSendSuppressed):
        module.eligible_result(path, time.time() - 60)


@pytest.mark.parametrize("field", ["confirmed", "results_agreed", "sha_match"])
def test_disputed_agreement_suppresses_send(tmp_path, field):
    module = _module()
    doc = _clean_doc()
    doc["mutual_agreement"][field] = False
    path = _write(tmp_path, doc)
    with pytest.raises(module.CountedSendSuppressed):
        module.eligible_result(path, time.time() - 60)


def test_recipient_is_exactly_the_lecturer_address():
    module = _module()
    assert module.RECIPIENT == LECTURER_RECIPIENT
    source = Path("scripts/send_counted_report.py").read_text(encoding="utf-8")
    assert FRIENDLY_RECIPIENT not in source


def test_friendly_send_utility_still_takes_an_explicit_recipient():
    names = send_gmail_report.__code__.co_varnames[:3]
    assert names == ("recipient", "artifact", "idempotency_key")
    assert _module().RECIPIENT != FRIENDLY_RECIPIENT


def test_stale_counted_result_is_not_resent(tmp_path):
    module = _module()
    path = _write(tmp_path, _clean_doc())
    assert module.eligible_result(path, time.time() + 60) is None


def test_idempotency_key_is_stable_per_settlement():
    module = _module()
    doc = _clean_doc()
    key = module.idempotency_key(doc)
    assert key == module.idempotency_key(doc)
    assert doc["mutual_agreement"]["sha256"] in key
