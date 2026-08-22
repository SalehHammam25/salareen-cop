"""Subgame-scoped selection of inbound peer audits.

A stale audit must never be mistaken for the current subgame's audit. Tagged
envelopes are matched on every tag they carry; untagged envelopes stay
acceptable for backward compatibility, but only while this subgame's audit
window is actually open, never from the backlog left by an earlier subgame.
"""

import logging
import time

from .wire import clean_audit

LOG = logging.getLogger("salareen.official")
TAG_KEYS = ("sub_game", "sub_game_number")


def tags_of(candidate: dict) -> list[int]:
    """Return the subgame tags present on an audit envelope."""
    return [candidate[key] for key in TAG_KEYS if key in candidate]


def matches(candidate: dict, sub_game: int, *, allow_untagged: bool) -> bool:
    """True when every tag present equals this subgame.

    Two tags that disagree can never both equal ``sub_game``, so a
    contradictory envelope is rejected without a special case.
    """
    present = tags_of(candidate)
    if not present:
        return allow_untagged
    return all(tag == sub_game for tag in present)


def _usable(raw: object) -> dict | None:
    """Return a per-subgame audit, discarding series-consensus envelopes."""
    candidate = clean_audit(raw)
    if candidate is None or candidate.get("consensus_sha") is not None:
        return None
    return candidate


def sweep_backlog(transport, sub_game: int) -> dict | None:
    """Drain audits queued before the window opened.

    Anything untagged here predates this subgame's audit exchange, so it is
    stale by definition and must not terminate this subgame.
    """
    found = None
    while (raw := transport.poll_audit(0.0)) is not None:
        candidate = _usable(raw)
        if candidate is None:
            continue
        if found is None and matches(candidate, sub_game, allow_untagged=False):
            found = candidate
            LOG.info("audit accepted sub_game=%s source=backlog", sub_game)
        else:
            LOG.info(
                "audit ignored sub_game=%s tags=%s source=backlog",
                sub_game,
                tags_of(candidate),
            )
    return found


def await_window(transport, sub_game: int, audit_wait: float) -> dict | None:
    """Wait out this subgame's audit window, ignoring mismatched envelopes.

    Call :func:`sweep_backlog` before announcing our own audit; anything that
    lands after that announcement is genuinely inside the window, so an
    untagged envelope here is still trusted for backward compatibility.
    """
    deadline = time.monotonic() + audit_wait
    while time.monotonic() < deadline:
        raw = transport.poll_audit(deadline - time.monotonic())
        if raw is None:
            return None
        candidate = _usable(raw)
        if candidate is None:
            continue
        if matches(candidate, sub_game, allow_untagged=True):
            LOG.info("audit accepted sub_game=%s source=window", sub_game)
            return candidate
        LOG.info(
            "audit ignored sub_game=%s tags=%s source=window",
            sub_game,
            tags_of(candidate),
        )
    return None
