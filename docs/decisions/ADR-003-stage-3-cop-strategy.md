# ADR-003: Stage 3 Cop Strategy Boundary

**Status:** Owner approved
**Owner:** Areen
**Review:** Codex-assisted adversarial review plus automated verification; independent human reviewer not required

## Decision

The cop strategy pursues the thief and may place barriers to reduce escape routes. It is not a renamed thief escape policy. Strategy receives immutable local state, returns a typed proposal, and cannot mutate Base Logic. Every proposal is revalidated by deterministic rules. Tie-breaking and fallback ordering are stable and testable. Reinforcement learning and LLM movement selection are excluded unless a later explicit owner decision changes scope.
