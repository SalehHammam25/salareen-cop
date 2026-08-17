# ADR-004: Stage 4 Shared Scent, Language, and Belief

**Status:** Owner approved
**Owner:** Areen
**Review:** Codex-assisted adversarial review plus automated verification; independent human reviewer not required

## Decision

Cop and thief must use byte-for-byte compatible scent configuration and mathematically identical emission, decay, overlap aggregation, clipping, edge handling, and turn ordering. Annex F fixes center intensity 0.9, decay 0.10, and field size 5x5. Natural-language messages may not communicate direct numeric coordinates. The cop maintains its own belief about the thief; it does not reuse the thief's inverse belief objective. Provider/LLM output is isolated to verbal text and cannot choose or validate actions.
