# ADR-005: Stage 5 Stable ngrok Boundary

**Status:** Owner approved; two-machine acceptance pending
**Owner:** Areen
**Review:** Codex-assisted adversarial review plus automated verification; independent human reviewer not required

## Decision

Use ngrok with an owner-assigned stable development domain. The domain, opponent endpoint, and authentication token remain private and must never appear in Git, logs, diagnostics, process arguments, or reports. Endpoint exchange is manual/private. Match the thief's bounded retry, pause, watchdog, conservative attribution, redaction, exact resume identity, and idempotent shutdown behavior. Resume requires equal game ID, session ID, protocol version, turn index, and phase. Mismatch aborts without inventing a winner. Reachability is not authentication.

Final Stage 5 acceptance remains blocked until a compatible cop implementation and second machine provide bidirectional calls and a complete match.
