# Local live-match gate evidence

Date: 2026-08-18. Scope: localhost only; no ngrok, public domain, PR, merge, or
Stage 6 activity.

Command: `uv run python tests/support/live_match_gate.py --repeat 2`

Result: PASS. Both canonical runs matched for every scenario. Coordinate and
barrier captures applied 12 actions; trapped capture applied 32; boundary
capture applied 36; survival applied exactly 35. Capture scores were `(20, 5)`
and survival scores were `(5, 10)` on both peers. Acknowledged restart and
terminal restart completed with 12 applications per peer. Lost acknowledgement
replayed `action-0` from the journal and still applied 12 unique actions.

Mismatch ended without outcome/score after two already accepted actions. Retry
exhaustion and watchdog expiry ended without outcome/score after one accepted
action. Attribution remained `unknown`. Every scenario used separate journals
and logs; `finally` reaped both child processes and verified ports 8801/8802
closed. The harness compared accepted action IDs/order, turn-bearing recovery
decisions, outcomes, scores, duplicate decisions, and application counts while
excluding timestamps, PIDs, elapsed timings, and temporary paths.

Adversarial review found and corrected a survival shutdown race: terminal
reconciliation could begin before the final scent/language boundary completed.
The cop now waits for both final Stage 4 messages before reconciliation.

Remaining: authorized ngrok/public endpoint checks, two-computer symmetric MCP
calls with Saleh, one reconciled remote match, redacted remote evidence, PR
review/merge, and Stage 6. These remain unchecked.

## Windows manual-failure correction

Areen reported a manual failure on 2026-08-18 at the old combined restart
assertion, with runtime `live-gate-j9l3y4fs`. That directory was not present in
the shared workspace when diagnosis began, and the old harness discarded
stdout/stderr, so the original failing peer cannot be recovered from evidence.
The failure remains recorded and is not treated as a pass.

Independent stress runs reproduced the same assertion family. In retained run
`live-gate-2iathnzs`, both peers timed out after `terminal_agreed`: cop never
completed the next unbounded score RPC and thief waited for shutdown. Other
retained adversarial runs exposed a Windows `WinError 10054` while observing
peer closure, recovery phase overwrite during an in-flight action, premature
restart before the receiver emitted `paused`, and schedule-dependent recovery
event turns/actions.

Corrections:

- every FastMCP operation now has an application timeout and terminal, score,
  shutdown, and capture RPCs use bounded identical-message retries;
- an aborted session cannot be changed back to paused by an in-flight retry;
- terminal peers use shutdown agreement plus observed peer-port closure, with
  Windows connection reset treated as closure;
- restarts require the receiver's structured `paused` event and confirmed old
  port release;
- recovery event turns are pinned to the negotiated resume boundary;
- each process generation captures stdout/stderr, and failures report role,
  PID, exit code, timeout, final event, output tails, bound port, and targeted
  terminate/kill/reap action.

Final corrected evidence: acknowledged restart passed 5 consecutive runs;
lost-ack, mismatch, retry exhaustion, watchdog, and terminal restart each
passed two consecutive runs. Two complete independent commands passed using
fresh roots `live-gate-yswgq_ns` (790.6 s) and `live-gate-37n6x7n3` (789.6 s).
Afterward ports 8801/8802 and exact peer-runner process counts were both zero.
The local-only gate is PASS again on this Windows environment.

## Second independent Windows failure and candidate correction

Areen reopened the gate after `terminal_restart` failed in retained runtime
`live-gate-95gu2_ka/terminal-0`, waiting for optional `hint-11`. Both journals
agreed at turn 10: cop had applied `action-9`; thief held pending `action-10`.
Thief had sent scent/hint 10 and cop received them. Resume had not been tried.
The fixed 30-second wait expired during valid Stage 4 progress, while the old
one-second Stage 4 wait also incorrectly persisted `paused_recovering`.

The correction persists/restores scent, belief, cadence, last scent/hint turns,
and token consumption; bounds Stage 4 calls; guards recovery phase changes by
epoch; and restores active phase only at the mandatory boundary. Terminal and
recovery interruptions now wait for `stage4_boundary_complete`, never optional
hints. Flushed progress reports runtime/repeat/scenario/status/time; failures
include exact command, PID, exit, timeout, last event, output tails, port, and
targeted cleanup.

All manual and stress failure directories remain preserved. Final focused
`terminal_restart` passed 20/20 at `live-gate-c0fbrjz1` (862.9 s). Each recovery
family passed five focused runs. Three complete gates passed at
`live-gate-b2vgdxol` (973.4 s), `live-gate-7ohfkm_i` (993.2 s), and
`live-gate-tt9qm2dj` (964.3 s), with identical evidence. Status is **candidate
PASS pending Areen's manual rerun**, not final PASS.
