"""Interrupted-process scenarios for the local live-match gate."""

from pathlib import Path

from operator_process import assert_clean
from process_diagnostics import wait_event, wait_exit, wait_success


def restart(runtime: Path, mode: str, make_peers, canonical) -> dict:
    recovery = {"SALAREEN_MAX_RETRIES": "20", "SALAREEN_WATCHDOG_TIMEOUT": "90"}
    cop_env = {**recovery, "SALAREEN_ACTION_DELAY": "2"}
    thief_env = dict(recovery)
    if mode == "lost_ack":
        thief_env["SALAREEN_CRASH_AFTER_SEND"] = "0"
    peers = make_peers(runtime, "capture", {"cop": cop_env, "thief": thief_env})
    thief, cop = peers
    try:
        from live_match_gate import start
        start(peers)
        if mode == "lost_ack":
            wait_exit(thief, 10)
            wait_event(cop, "paused")
        else:
            wait_event(thief, "stage4_boundary_complete",
                       correlation="action-0", timeout=60)
            thief.stop()
            wait_event(cop, "paused")
        thief.extra_env = {}
        thief.start()
        wait_success(peers, 120)
        result = canonical(peers)
        assert result["terminal"] == "cop_capture" and result["score"] == [20, 5]
        return result
    finally:
        assert_clean(peers)


def negative(runtime: Path, mode: str, make_peers, canonical) -> dict:
    release = runtime / "mismatch.release"
    cop_env = ({"SALAREEN_VERIFICATION_BARRIER_TURN": "1",
                "SALAREEN_VERIFICATION_BARRIER_RELEASE": str(release)}
               if mode == "mismatch" else {"SALAREEN_ACTION_DELAY": "30"})
    if mode == "retry_exhaustion":
        cop_env.update(SALAREEN_MAX_RETRIES="2", SALAREEN_RETRY_BACKOFF="0.05")
    if mode == "watchdog":
        cop_env.update(SALAREEN_MAX_RETRIES="100", SALAREEN_RETRY_BACKOFF="0.05",
                       SALAREEN_WATCHDOG_TIMEOUT="0.1")
    peers = make_peers(runtime, "capture", {"cop": cop_env})
    thief, cop = peers
    try:
        from live_match_gate import start
        start(peers)
        wait_event(thief, "stage4_boundary_complete",
                   correlation="action-0", timeout=60)
        if mode == "mismatch":
            wait_event(cop, "strategy_blocked", correlation="action-1", timeout=60)
        thief.stop()
        if mode != "mismatch":
            wait_event(cop, "paused", timeout=60)
        if mode == "mismatch":
            thief.extra_env = {"SALAREEN_RECOVERY_MISMATCH": "game_id"}
            thief.start()
            wait_event(thief, "recovery_rejected")
            release.write_text("release\n", encoding="utf-8")
            wait_exit(thief, 30, fallback=True)
        kind = {"retry_exhaustion": "recovery_exhausted",
                "watchdog": "watchdog_expired", "mismatch": "message_rejected"}[mode]
        wait_event(cop, kind, timeout=60)
        wait_exit(cop, 30, fallback=True)
        result = canonical(peers)
        assert result["terminal"] is None and result["score"] == [None, None]
        return result
    finally:
        assert_clean(peers)


def terminal_restart(runtime: Path, make_peers, canonical) -> dict:
    recovery = {"SALAREEN_MAX_RETRIES": "20", "SALAREEN_WATCHDOG_TIMEOUT": "90"}
    peers = make_peers(runtime, "capture", {
        "cop": {**recovery, "SALAREEN_ACTION_DELAY": "2"}, "thief": recovery})
    thief, cop = peers
    try:
        from live_match_gate import start
        start(peers)
        wait_event(thief, "stage4_boundary_complete",
                   correlation="action-10", timeout=60)
        thief.stop()
        wait_event(cop, "paused")
        thief.start()
        wait_success(peers, 120)
        result = canonical(peers)
        assert result["terminal"] == "cop_capture" and result["score"] == [20, 5]
        return result
    finally:
        assert_clean(peers)
