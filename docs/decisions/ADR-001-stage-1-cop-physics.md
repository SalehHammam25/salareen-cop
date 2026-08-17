# ADR-001: Stage 1 Cop Physics

**Status:** Owner approved
**Owner:** Areen
**Review:** Codex-assisted adversarial review plus automated verification; independent human reviewer not required

## Decision

- Reject off-board movement deterministically without mutation.
- Require `max_moves == survival_threshold` for an accepted Stage 1 configuration.
- Route coordinate overlap, barrier-on-thief, and trapped-thief capture through one local Capture Claim boundary.
- Permit a cop to place a barrier on its own cell. Its current occupancy is grandfathered until it leaves; neither peer may subsequently enter that barrier cell.
- `STAY` is not a legal escape destination and does not prevent trapped-thief capture.
- Evaluate capture before survival when both become true on the same transition.
- Load Stage 1 from validated shared `config/game.json` values.

These decisions match the thief's shared physics contract while preserving cop-only barrier authority. They resolve the five former PRD-01 questions and two transition-order ambiguities; they do not authorize implementation on this branch.
