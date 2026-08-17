# ADR-006: Cop Live-Match Composition

**Status:** accepted; implementation pending

**Owner:** Areen
**Review:** Codex-assisted adversarial review and automated documentation verification; independent human review not required

## Decision

Adopt `docs/contracts/live-match-orchestration-v1.md` as the shared production design. The cop repository will own an independent cop runner that composes its local configuration, Base Logic, cop strategy, transport, scent/language/belief, recovery and structured log. There will be no central runner or shared runtime state.

The current strict six-field geometry contract remains unchanged. Additional orchestration messages are separately versioned. The cop accepts game messages only from its configured thief role; this is Stage 5 protocol validation, not authentication.

Remote opponent endpoints use HTTPS, the configured exact host/permitted port and exact `/mcp` path, with no userinfo, query, fragment, localhost or private address. The stricter rule replaces any earlier implication that a query could merely be redacted.

Stage 5 contains no hashing, signatures, Nonces, Commit-Reveal or cryptographic Capture Claim proof. Those remain Stage 6 work.

## Consequences

- The production cop runner and all missing adapters/tests remain unchecked implementation work.
- Capture Claim disagreement in Stage 5 aborts safely with evidence; it is not cryptographically adjudicated.
- The PDF's incomplete wire choreography is resolved narrowly by owner-approved sequential thief-first turns consistent with existing Base Logic.
- Shared contract and future fixtures must remain byte-identical with the thief repository.

## Adversarial review

The decision rejects central-server behavior, shared state, hidden opponent truth, simultaneous-action ambiguity, double application, lost-acknowledgement divergence, combined barrier/movement actions, survival-before-capture races, Stage 4 ordering drift, invented technical-loss blame, premature cryptography, endpoint divergence and claims of authenticated security.
