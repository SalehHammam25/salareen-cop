# Live-match orchestration verification

Branch: `feat/live-match-orchestration`

- `uv lock`: exit 0; 88 packages resolved.
- `uv sync --frozen`: exit 0; 86 packages checked.
- `uv run ruff check .`: exit 0.
- `uv run pytest -q`: exit 0; 436 passed, one dependency deprecation warning.
- `uv run python scripts/check_python_line_lengths.py`: exit 0; 155 files,
  maximum 150 lines.
- Local process probe: exit 0; thief-first, four turns, two applications at
  each receiver, duplicate response replayed, outcome `cop_capture`, Annex F
  scores cop 20/thief 5.
- Stage 4 production capture rerun: scent then template language then next-turn
  belief barrier; shutdown at turn 12 with independent logs.
- Acknowledged-action restart: killed thief after action 0 boundary; cop paused;
  exact resume completed without reapplication.
- Lost acknowledgement: sender interrupted after remote application; exact
  pending-ack resume retransmitted identical `action-0`; receiver recorded
  `duplicate_replayed`; sender applied once.
- Barrier-on-thief production capture completed and reconciled 20/5.
- Shutdown check: ports 8801 and 8802 closed.
- Production composition follow-up: the autonomous peer-owned capture scenario
  reached coordinate overlap at turn 12, reconciled capture, scores 20/5 and
  shutdown. The survival scenario reached exactly 35 accepted Base Logic actions,
  reconciled scores 5/10 and shutdown. Separate JSONL logs and journals were used.
- The accepted shared contract source identity is
  `81bea39ce3516117541b5b2a471bf211d6303df6`; the earlier expected hash was stale.

No ngrok, external endpoint, credential, Stage 6 primitive or shared runtime
database was used.
