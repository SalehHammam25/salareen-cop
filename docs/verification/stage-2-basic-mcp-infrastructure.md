# Stage 2 Basic MCP Infrastructure Verification

Date: 2026-08-17

## Delivery context

- Branch: `feat/cop-stage-2-mcp-infrastructure`, stacked directly on
  `feat/cop-stage-1-base-logic`.
- Stage 1 base commit:
  `501f590050b18c03685339cad61873a8ce1d582f`.
- Stage 1 was not merged because the GitHub Pull Request interface was unavailable.
- No Pull Request or merge was performed for Stage 2.
- The requested ADR filename did not exist. The repository's corresponding authority,
  `docs/decisions/ADR-002-stage-2-shared-transport.md`, was used and the mismatch
  remains recorded rather than silently resolved.
- The sibling `salareen-thief` repository was inspected read-only.

## Contract evidence

- Protocol: `1.0-provisional`.
- Transport: FastMCP Streamable HTTP at `/mcp`.
- Tools: `receive_geometry` and `relay_geometry`.
- Envelope keys are exactly `protocol_version`, `correlation_id`,
  `sender_role`, `x`, `y`, and `step`.
- The canonical fixture has the same Git object ID in both repositories:
  `5f1c025c8f1a9944e4daeb66d490ae98e29d0a20`.
- Locked versions include FastMCP 2.14.7 and MCP 1.29.0.

## Versions and final commands

Every final command below exited 0.

- `uv --version`: `uv 0.12.5 (210d1f678 2026-08-14 x86_64-pc-windows-msvc)`.
- `python --version`: `Python 3.12.10`.
- `uv lock`: resolved 88 packages.
- `uv sync --frozen`: checked 86 packages.
- `uv run python -c "import salareen_cop; import salareen_cop.base_logic"`:
  imports succeeded.
- `uv run ruff check .`: all checks passed.
- `uv run pytest -q`: 249 passed, one upstream Authlib deprecation warning.
- `uv run python scripts/check_python_line_lengths.py`: checked 62 Python
  files; maximum 150 lines.
- `git diff --check`: clean.

Focused verification:

- Focused Stage 2 files: 48 passed.
- Two consecutive separate-process integration executions: 2 passed; both child
  processes were terminated and reaped by test assertions.
- Stage 1 suite with all Stage 2 test files ignored: 201 passed.
- Forbidden Stage 1 dependency scan found no FastMCP, MCP transport, networking,
  socket, or asyncio imports under `src/salareen_cop/base_logic`.
- Credential and public-endpoint scan found no token, API-key, private-key, ngrok
  endpoint, or client-secret patterns in the changed implementation boundary.
- The fixture scan found no `session_id`, `phase`, or `turn_index` wire fields.

## Intermediate failures and corrections

1. The first `uv sync --frozen` exited 1 because OneDrive rejected uv's hardlink
   operation while installing Typer. `uv sync --frozen --link-mode copy` completed
   successfully; the exact requested command was then rerun and exited 0.
2. A parallel uv verification attempt exited 1 with Windows `Access is denied`.
   Checks were rerun sequentially.
3. A sandboxed direct virtual-environment test run produced one process-integration
   failure because its Windows Store Python subprocess could not launch. Running the
   same suite through `uv run pytest -q` outside that sandbox constraint passed,
   including repeated fresh-process runs.

## Adversarial review

- Shared production modules and the canonical fixture were compared against the
  thief peer; cop-specific tests retain `sender_role: "cop"`.
- Strict validation precedes state use, and rejected or mismatched duplicate
  messages preserve the immutable orchestrator state.
- Identical duplicates reuse the accepted result. Accepted history is FIFO,
  process-local, session-bound, and defaults to capacity 100.
- Timeouts, retries, backoff, watchdog boundaries, cancellation propagation,
  disconnect typing, exception-detail suppression, client cleanup, and child-process
  cleanup have deterministic tests.
- No Stage 1 reverse dependency, circular transport import, shared mutable
  cross-process state, extra wire field, private endpoint, or secret was found.
- Remote technical-loss attribution remains unresolved as required by MCP-BQ-03.

## Remaining gate

`MCP-065` remains unchecked. Stage 2 is not complete under the governance gate
until its Pull Request can be reviewed and merged after Stage 1.
