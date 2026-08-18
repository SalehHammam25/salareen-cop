# Project Implementation Plan

**Status:** Stages 1-5 documentation aligned; implementation not started
**Repository:** `salareen-cop`
**Specification:** 3.0.0
**Owner:** Areen

## Authority and governance

The requirements PDF controls. Appendix E controls mandatory-rule coverage and Annex F controls numerical values. ADRs record owner-approved interpretations where the PDF is ambiguous or where both peers require one exact contract. The thief repository is compatibility evidence only.

Independent human review is not required under the owner-approved policy. Every stage still requires a focused branch, Pull Request, Codex-assisted adversarial review, automated verification, recorded evidence, and a clean synchronized `main` before the next stage.

## Lifecycle

`PRD -> ADR -> PLAN -> TODO -> traceability review -> implementation -> automated verification -> adversarial review -> PR -> merge`

Implementation files must remain separate from documentation, deterministic rules must remain separate from LLM/provider behavior, invalid inputs must reject without mutation, secrets must never enter Git, and every future Python file must remain at or below 150 lines.

## Stage order and gates

The Chapter 10 order is recommended by the specification and adopted as project policy:

1. Base Logic
2. Basic MCP Infrastructure
3. Blind Cop Strategy
4. Language, Scent, and Belief
5. Cloud Exposure and Tunneling
6. Security and Cryptography (future)
7. Reporting and Visualization Shell (future)

Each stage must work end-to-end before its successor begins. Stages 6-7 retain future-stage stubs and are outside this alignment scope.

## Stage 1 - Base Logic

Build a deterministic, local, single-process rules engine from validated shared configuration. Implement board state, orthogonal movement and STAY, cop-only permanent barriers, all capture paths through the common local Capture Claim boundary, survival, technical-loss representation, and fixed scoring. Apply ADR-001: off-board rejection without mutation; equal `max_moves` and `survival_threshold`; grandfathered immediate cop occupancy on a newly placed own-cell barrier; STAY does not defeat trapped capture; capture precedes survival. No networking or strategy enters this stage.

Gate: PRD-01 acceptance criteria and Appendix E rules 11-16 and 46-48 are covered by deterministic tests; Annex F Tables 13, 15, and 17 are enforced; shared configuration produces repeatable state; all rejected actions preserve state.

## Stage 2 - Basic MCP Infrastructure

Run cop and thief as wholly separate FastMCP server/client processes using Streamable HTTP. Adopt the exact `1.0-provisional` geometry fixture and strict fields only: `protocol_version`, `correlation_id`, `sender_role`, `x`, `y`, `step`. Expose `receive_geometry` and `relay_geometry`; keep session and phase local, route transport through one orchestrator, reject illegal phases, bound waits/retries, and implement the shared FIFO-100 duplicate policy. No shared runtime state or remote-blame inference.

Gate: two separate localhost processes both serve and call; the shared fixture decodes identically; malformed, unknown-version, stale, out-of-phase, and duplicate-mismatch messages reject without mutation; Appendix E rules 1-9 are owned.

## Stage 3 - Blind Cop Strategy

Add a deterministic cop policy behind a strategy boundary. The cop pursues likely thief positions and may spend barriers to contain escape routes; it must not copy the thief's escape objective. Every proposal passes through Base Logic validation. Tie-breaking and fallbacks are typed and deterministic. Reinforcement learning is excluded unless separately approved.

Gate: legal pursuit/barrier proposals, deterministic repeatability, adversarial fallback coverage, no LLM movement authority, and no Stage 4 dependencies.

## Stage 4 - Language, Scent, and Belief

Match the shared thief scent arithmetic exactly: fixed center intensity 0.9, fixed decay 0.10, fixed 5x5 emission field, overlap aggregation, clipping, edge behavior, and transition ordering. Add natural-language hints with a negotiable maximum default of 15 words, forbid numeric coordinate communication, and maintain a cop-specific belief over thief location. Provider output may create verbal text only and cannot directly select actions.

Gate: cross-peer scent fixtures agree exactly; hint validation and token accounting are deterministic; belief remains normalized; cop decisions consume belief through the Stage 3 boundary; Appendix E rules 25-27 are owned.

## Stage 5 - Cloud Exposure and Tunneling

Expose the local Streamable HTTP endpoint through ngrok using an owner-assigned stable development domain supplied privately. Never store the domain, opponent endpoint, or authentication token. Match the thief's pause, retry, watchdog, redaction, failure-attribution, exact resume-identity, and idempotent shutdown contracts. Reachability is not authentication; Stage 6 owns trust.

Gate: local and fake-provider verification passes; public endpoint checks are redacted; reconnect reuses the stable domain; resume requires exact game/session/protocol/turn/phase equality; final gate remains blocked until two independent machines complete a bidirectional match.

## Cross-stage traceability

Every TODO task has a stable stage ID and cites its PRD section or acceptance criterion. Each PRD contains an Appendix E/Annex F table. Verification must check unique task IDs, no unresolved markers, documentation/code scope, numeric authority, secret absence, and exact shared fixture compatibility.

## Known specification tensions

Do not silently resolve the series count conflict (`num_games: 1` example versus Annex F fixed 6), the one-counted-game-per-opponent rule, simplified versus full commitment examples, or differing timeout examples. Stages 1-5 use only decisions explicitly recorded in ADRs; later-stage contradictions remain open until their owning stage.

## Live-match composition recovery plan

The Stage 1-5 components are not yet a playable system. ADR-006 and `docs/contracts/live-match-orchestration-v1.md` define the production composition. Implementation order is shared schemas/fixtures, expected-role and endpoint convergence, cop runner/adapters, thief runner compatibility, exactly-once/recovery wiring, deterministic localhost matches, then authorized remote proof. Every runner remains peer-local; no central coordinator is allowed. Stage 6 security primitives and Stage 7 reporting remain excluded.

## Stage 6-7 execution addendum

Implement the minimum mandatory security path symmetrically on a dedicated
feature branch: shared canonical contracts first, then Ed25519 configuration and
Step-0 signatures, commit/acknowledge/reveal, capture verification, chained logs,
and final nonce audit. After focused security tests pass, add six-game series
artifacts, exact peer-result agreement, verified replay, and a privacy-safe view
model. Preserve all earlier behavior and run full suites plus the live/security
gate before local commits. External key exchange and remote peer access are
recorded separately and do not block local implementation.
