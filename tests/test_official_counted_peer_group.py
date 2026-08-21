"""Counted reporting follows the declared peer group and never assumes one."""

import pytest

from salareen_cop.official.reporting import build_counted_result
from salareen_cop.official.terms import GROUP_ID
from tests.test_counted_reporting import PEER, _series

GROUPS = ["GRP00001", "amireman", "zeta.group-9", "a"]


@pytest.mark.parametrize("group", GROUPS)
def test_counted_result_follows_the_declared_peer_group(group):
    series = _series()
    series.peer_identity = {**series.peer_identity, "group_id": group}
    series.game_id = f"NC-{group}"
    doc = build_counted_result(series, PEER)
    assert set(doc["groups"]) == {GROUP_ID, group}
    assert doc["group_details"]["group_2"]["group_id"] == group
    for row in doc["sub_games"]:
        assert set(row["score"]) == {GROUP_ID, group}


@pytest.mark.parametrize("missing", [None, "", GROUP_ID])
def test_counted_result_refuses_a_missing_or_self_peer_group(missing):
    series = _series()
    peer = dict(series.peer_identity)
    if missing is None:
        peer.pop("group_id", None)
    else:
        peer["group_id"] = missing
    series.peer_identity = peer
    with pytest.raises(ValueError, match="distinct peer group_id"):
        build_counted_result(series, PEER)
