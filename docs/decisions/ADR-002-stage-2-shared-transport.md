# ADR-002: Stage 2 Shared Transport Contract

**Status:** Owner approved
**Owner:** Areen
**Review:** Codex-assisted adversarial review plus automated verification; independent human reviewer not required

## Decision

Adopt the thief's committed `1.0-provisional` contract: exact tools `receive_geometry` and `relay_geometry`; FastMCP Streamable HTTP; and strict wire fields `protocol_version`, `correlation_id`, `sender_role`, `x`, `y`, `step`. Do not add `session_id`, game ID, phase, or turn fields to this Stage 2 envelope. Session and phase remain process-local.

Identical validated duplicates return the same result without a second mutation. Reuse of a correlation ID with different validated content returns `DUPLICATE_MISMATCH` without mutation. History is deterministic, process-local, FIFO-bounded to 100. Both peers are separate server/client processes with no shared runtime state. Transport failures remain typed local results and do not assign remote blame.
