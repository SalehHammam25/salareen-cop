"""Interrupted-process scenarios for the local live-match gate."""

from pathlib import Path

from operator_process import assert_clean, wait_event


def restart(runtime: Path, mode: str, make_peers, canonical) -> dict:
    cop_env = {"SALAREEN_ACTION_DELAY": "0.4"}
    thief_env = {"SALAREEN_CRASH_AFTER_SEND": "0"} if mode == "lost_ack" else {}
    peers = make_peers(runtime, "capture", {"cop": cop_env, "thief": thief_env})
    thief, cop = peers
    try:
        from live_match_gate import start
        start(peers)
        if mode == "lost_ack":
            thief.wait_exit(10)
            wait_event(cop, "paused")
        else:
            wait_event(thief, "hint_sent", correlation="hint-1")
            thief.stop()
        thief.extra_env = {}
        thief.start()
        assert thief.wait_exit(40) == 0 and cop.wait_exit(40) == 0
        result = canonical(peers)
        assert result["terminal"] == "cop_capture" and result["score"] == [20, 5]
        return result
    finally:
        assert_clean(peers)


def negative(runtime: Path, mode: str, make_peers, canonical) -> dict:
    cop_env = {"SALAREEN_ACTION_DELAY": "0.3"}
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
        wait_event(thief, "hint_sent", correlation="hint-1")
        thief.stop()
        if mode == "mismatch":
            thief.extra_env = {"SALAREEN_RECOVERY_MISMATCH": "game_id"}
            thief.start()
            wait_event(thief, "recovery_rejected")
            thief.wait_exit(10)
        kind = {"retry_exhaustion": "recovery_exhausted",
                "watchdog": "watchdog_expired", "mismatch": "message_rejected"}[mode]
        wait_event(cop, kind)
        cop.wait_exit(10)
        result = canonical(peers)
        assert result["terminal"] is None and result["score"] == [None, None]
        return result
    finally:
        assert_clean(peers)


def terminal_restart(runtime: Path, make_peers, canonical) -> dict:
    peers = make_peers(runtime, "capture", {"cop": {"SALAREEN_ACTION_DELAY": "0.2"}})
    thief, cop = peers
    try:
        from live_match_gate import start
        start(peers)
        wait_event(thief, "hint_sent", correlation="hint-11", timeout=30)
        thief.stop()
        thief.start()
        assert thief.wait_exit(30) == 0 and cop.wait_exit(30) == 0
        result = canonical(peers)
        assert result["terminal"] == "cop_capture" and result["score"] == [20, 5]
        return result
    finally:
        assert_clean(peers)
