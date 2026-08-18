# Stage 5 Cloud Exposure and ngrok Tunneling Verification

Date: 2026-08-17

## Delivery and external status

- Branch: `feat/cop-stage-5-cloud-tunneling`, stacked directly on
  `feat/cop-stage-4-language-scent`.
- Stage 4 base commit:
  `5e8c79f366af228dc22c66c850c392dbc4e58fa2`.
- Stages 1-4 remain unmerged while GitHub Pull Requests are unavailable.
- No Pull Request or merge was performed, and Stage 6 was not started.
- The thief repository was inspected read-only at compatibility commit
  `4490222`.
- The requested ADR filename does not exist. The actual authority used was
  `ADR-005-stage-5-stable-ngrok-boundary.md`.

No real public cop test ran. This session had no separately supplied cop stable
domain, no confirmed authenticated ngrok installation, and no explicit owner
authorization for a public test. No external service was started.

## Architecture and private boundary

- `TunnelProvider` defines provider-neutral async start, health, and stop.
- `NgrokProvider` is the production adapter. It waits for local cop `/mcp`
  readiness, checks ngrok version and authenticated-agent readiness, starts one
  argument-list subprocess without a shell, verifies the exact assigned URL from
  the local ngrok agent API, probes public `/mcp`, and reaps the process.
- The subprocess is equivalent to
  `ngrok http <LOCAL_PORT> --url https://<ASSIGNED_DOMAIN>`.
- `NGROK_DOMAIN`, `SALAREEN_OPPONENT_URL`, and the explicit local port are
  private runtime inputs. The application has no authentication-token field,
  token environment variable, token argument, or ngrok configuration reader.
- Endpoint validation requires public HTTPS and rejects localhost/private IP,
  userinfo, query, fragment, unsafe port, and malformed values.
- Endpoint and error representations suppress private URLs and exception details.

## Recovery and attribution

- Bounded retry/backoff propagates cancellation and yields one typed exhaustion.
- Gameplay remains paused during disconnect/retry. Watchdog expiry aborts.
- Resume requires exact game ID, session ID, protocol version, turn index, and
  phase. Any mismatch aborts without assigning a winner.
- Recovery reuses the same assigned domain. Stage 2 duplicate handling prevents
  an already acknowledged message from mutating state again.
- Verified local server/tunnel failure may produce local technical loss.
  Verified remote application failure with a healthy local path may produce
  remote technical loss. DNS, TLS, Internet, provider, and ambiguous failures
  remain unknown pending Stage 6 audit.

## Verification

Every final command exited 0:

- `uv lock`: 88 packages resolved.
- `uv sync --frozen`: 86 packages checked.
- `uv run ruff check .`: all checks passed.
- `uv run pytest -q`: 426 passed with one upstream Authlib warning.
- Focused Stage 5 suite: 48 passed; 378 earlier-stage tests deselected.
- Stage 1-4 regressions with Stage 5 tests ignored: 378 passed.
- `uv run python scripts/check_python_line_lengths.py`: 137 Python files
  checked; maximum 150 lines.
- `git diff --check`: passed.
- Dependency isolation and reverse-import scans: no matches.
- Credential and real-domain scans: no production values found.
- Process inspection found no running ngrok process after fake lifecycle tests.

The largest Stage 5 production file is `ngrok_adapter.py` at 102 lines.
The largest Stage 5 test file is `test_stage5_ngrok_adapter.py` at 141 lines.
The redacted public helper is 112 lines.

## Failures and corrections

1. The compatibility implementation read a legacy tunnel-token environment
   field. The cop implementation removes that field and never reads application
   token material.
2. The compatibility endpoint validator allowed queries. The cop contract
   requires unsafe query rejection, so all remote endpoint queries now reject;
   the redactor remains available for diagnostic handling of arbitrary input.
3. The compatibility public helper discovered an account URL by starting random
   tunnels and launched a thief-role peer. It now requires private
   `NGROK_DOMAIN`, validates it before startup, and launches the cop role.
4. The copied runbook was thief-oriented. It was rewritten around the cop as the
   local operator while retaining symmetric second-machine instructions.
5. The first Ruff run found one import-layout issue in the public helper. A blank
   line correction resolved it; final Ruff passed.
6. Adversarial review added an explicit recovery test proving that a matching
   reconnect does not reapply an acknowledged Stage 2 message.

## External evidence still required

- A separately assigned stable cop domain and authenticated local ngrok agent.
- Authorized public cop health and Streamable HTTP tool verification.
- A second independent thief machine and distinct thief domain.
- Bidirectional public tool calls, disconnect/reconnect evidence, clean shutdown,
  and one complete remote match.
- Pull Request review and ordered merge after Stages 1-4.

Accordingly, CLD-056 through CLD-059, CLD-063, and CLD-065 remain unchecked.
CLD-060 records this blocker as complete.
