# Live-match orchestration verification

Branch: `feat/live-match-orchestration`

- `uv lock`: exit 0; 88 packages resolved.
- `uv sync --frozen`: exit 0; 86 packages checked.
- `uv run ruff check .`: exit 0.
- `uv run pytest -q`: exit 0; 429 passed, one dependency deprecation warning.
- `uv run python scripts/check_python_line_lengths.py`: exit 0; 146 files,
  maximum 150 lines.
- Local process probe: exit 0; thief-first, four turns, two applications at
  each receiver, duplicate response replayed, outcome `cop_capture`, Annex F
  scores cop 20/thief 5.
- Shutdown check: ports 8801 and 8802 closed.

No ngrok, external endpoint, credential, Stage 6 primitive or shared runtime
database was used.
