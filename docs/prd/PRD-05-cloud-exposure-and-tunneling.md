# PRD-05: Cloud Exposure and Tunneling

**Status:** Owner-approved requirements; implementation not started
**Specification:** 3.0.0
**Decision:** ADR-005

## Purpose

Expose the working cop FastMCP Streamable HTTP endpoint through a stable public ngrok domain and support safe remote operation without weakening process separation or leaking private infrastructure.

## Mandatory requirements

- Use a provider-neutral tunnel lifecycle with an ngrok production adapter.
- The assigned stable domain, opponent URL, and authentication material come only from ignored private configuration/environment.
- Never persist, print, commit, or pass an authentication token to a subprocess.
- Remote endpoints require public HTTPS and reject localhost, private IPs, userinfo, fragments, malformed ports, and unsafe components.
- Diagnostics redact credentials, secret query keys, and private endpoint values.
- Lifecycle provides bounded start/readiness/health/stop behavior and idempotent shutdown.
- Retry/backoff and watchdog settings come from agreed shared values and obey Annex F status.
- Defaults are a negotiable 30-second response timeout and negotiable 60-second watchdog; 30 requests/minute, concurrency 2, backoff 5 seconds, retries 3, and queue depth 100 are minimums.
- Gameplay pauses on disconnect and bounded recovery reuses the same stable domain.
- Resume requires exact game ID, session ID, protocol version, turn index, and phase.
- Resume mismatch aborts without inventing a winner.
- Failure attribution is conservative: verified local failure may be local technical loss; verified remote application failure with a healthy local path may be remote; provider/Internet/DNS/TLS/ambiguous failure stays unknown pending Stage 6.
- Endpoint reachability is not authentication.
- Both machines must expose and call through their own tunnels; no central server or shared state is introduced.

## Acceptance criteria

- **CLD-AC-01:** safe private configuration produces one stable public HTTPS endpoint.
- **CLD-AC-02:** invalid/unsafe endpoints reject and diagnostics redact sensitive parts.
- **CLD-AC-03:** lifecycle start/readiness/health/stop is bounded, typed, and idempotent.
- **CLD-AC-04:** DNS, TLS, disconnect, timeout, process exit, and provider errors never hang or leak exception secrets.
- **CLD-AC-05:** retries/backoff/watchdog use agreed values and propagate cancellation.
- **CLD-AC-06:** reconnect pauses gameplay, reuses the domain, and resumes only on exact identity equality.
- **CLD-AC-07:** mismatch and ambiguous attribution do not fabricate a winner.
- **CLD-AC-08:** no token, domain, opponent endpoint, or private configuration appears in Git or evidence.
- **CLD-AC-09:** cop and thief make symmetric public tool calls on independent machines.
- **CLD-AC-10:** a complete remote match succeeds; until then the final Stage 5 gate remains blocked.

## Authority matrix

| Source | Owned requirements |
|---|---|
| Appendix E 1-2 | independent environments and no shared runtime state |
| Appendix E 6-7 | bounded waits and watchdog/process monitoring |
| Appendix E 10 | public tunnel exposure |
| Annex F Table 19 | network/retry/watchdog values and statuses |
| ADR-005 | stable ngrok, privacy, resume, attribution, shutdown |

## Non-goals and blocker

No discovery service, central judge, cryptographic authentication, Commit-Reveal, Gmail, GUI, or reporting. Final acceptance requires a compatible implemented cop, the thief peer, two machines, and authorized network access.

## Live runner and strict endpoint extension

ADR-006 and the shared live-match contract own independent runner composition, exact-identity pause/resume, acknowledged-action protection, terminal reconciliation and controlled shutdown. Remote endpoints must use HTTPS, exact configured host/permitted port and `/mcp`, with no userinfo, query, fragment, localhost or private address. Expected-role checking is protocol validation only. The runner, adapters and full-match tests remain unimplemented.
