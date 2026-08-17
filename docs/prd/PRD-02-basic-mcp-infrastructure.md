# PRD-02: Basic MCP Infrastructure

**Status:** Owner-approved requirements; implementation not started
**Specification:** 3.0.0
**Decision:** ADR-002

## Purpose

Connect independently running cop and thief peers over localhost with symmetric FastMCP Streamable HTTP while preserving strict local truth and deterministic transport behavior.

## Mandatory contract

- Each peer is a separate process, configuration root, FastMCP server, and FastMCP client.
- No memory, mutable object, runtime file, or private configuration is shared.
- One orchestrator is the sole transport-state gateway.
- Protocol version is exactly `1.0-provisional`.
- Tool names are exactly `receive_geometry` and `relay_geometry`.
- The strict geometry envelope contains only `protocol_version`, `correlation_id`, `sender_role`, `x`, `y`, and `step`.
- Do not add session, game, phase, or turn fields to the envelope. Session and phase are local process state.
- Unknown and missing fields, wrong types, unsupported versions, invalid identifiers/roles/steps, stale messages, and illegal phases reject without mutation.
- Accepted results use `accepted: true` plus the validated message. Rejections use `accepted: false`, stable code, and deterministic detail.
- Identical duplicate requests return the same result without a second mutation.
- Same correlation ID with different validated content returns `DUPLICATE_MISMATCH`.
- Duplicate history is process-local deterministic FIFO with default bound 100.
- Legal phase transitions, deadlines, retries, and watchdog boundaries prevent indefinite waits.
- Annex F defaults are a negotiable 30-second response timeout and negotiable 60-second watchdog; backoff 5 seconds and retries 3 are minimums.
- Stage 2 reports typed local failure and does not infer remote technical-loss blame.
- Shared JSON owns negotiated network limits; private local endpoint configuration never enters Git.

## Acceptance criteria

- **MCP-AC-01:** the canonical thief fixture decodes and re-encodes exactly.
- **MCP-AC-02:** cop and thief run as separate localhost processes and both serve and call.
- **MCP-AC-03:** both tools use exact names and Streamable HTTP.
- **MCP-AC-04:** all malformed and incompatible envelopes reject deterministically without mutation.
- **MCP-AC-05:** legal phase transitions pass and illegal transitions reject.
- **MCP-AC-06:** identical duplicates are idempotent and content mismatches return `DUPLICATE_MISMATCH`.
- **MCP-AC-07:** FIFO eviction at 100 is deterministic and local to one session/process.
- **MCP-AC-08:** timeout/retry/watchdog exhaustion returns one typed local result.
- **MCP-AC-09:** tests prove no shared-memory/file shortcut and local-truth-only exposure.
- **MCP-AC-10:** fresh processes produce identical fixture results.

## Authority matrix

| Source | Owned requirements |
|---|---|
| Appendix E 1-2 | separate processes and no shared runtime state |
| Appendix E 3-7 | orchestrator, state machine, illegal-transition reporting, deadline tracker, watchdog |
| Appendix E 8-9 | local truth only; no omniscient live state |
| Annex F Table 19 | 30-second negotiable response, 60-second negotiable watchdog; retry/backoff minimums |
| ADR-002 | exact cross-repository protocol and idempotency contract |

## Non-goals and blocker

No public tunnel, strategy, scent/language, cryptography, reporting, or remote-blame attribution. Stage 5 owns public transport; Stage 6 owns authentication.
