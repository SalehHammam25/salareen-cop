# PRD-04: Language, Scent, and Belief

**Status:** Owner-approved requirements; implementation not started
**Specification:** 3.0.0
**Decision:** ADR-004

## Purpose

Add shared dynamic scent and natural-language evidence while maintaining a cop-specific probability belief over thief location and preserving deterministic movement authority.

## Mandatory requirements

- Both peers use exactly compatible scent configuration and arithmetic.
- Fixed values are center intensity 0.9, per-turn decay 0.10, and 5x5 emission field.
- Scent intensities remain bounded at zero; overlapping deposits aggregate in the same order and with the same arithmetic on both peers.
- Edge clipping does not wrap or renormalize the kernel.
- Transition ordering for decay, movement/STAY, emission, observation, belief update, and strategy consumption is explicit and shared.
- Each peer reads only the opponent scent field.
- Natural-language hints are free-form words, not direct numeric coordinates or a numeric location protocol.
- Hint limit defaults to negotiable 15 words and applies consistently to templates and providers.
- The cop belief represents probability of thief location, excludes impossible cells, normalizes deterministically, and degrades safely on contradictory/invalid evidence.
- Language and scent evidence carry explicit reliability boundaries.
- Provider failures return typed fallback text.
- Provider/LLM output cannot directly create or validate a movement/barrier action.
- Token use is accounted for without exposing secrets.

## Acceptance criteria

- **LSB-AC-01:** canonical scent fixture matches the thief exactly for emission, decay, overlap, clipping, and ordering.
- **LSB-AC-02:** fixed Annex F scent values cannot be overridden.
- **LSB-AC-03:** edge/corner emission clips without wrap or renormalization.
- **LSB-AC-04:** STAY follows the same decay/emission ordering as movement.
- **LSB-AC-05:** valid hints obey the negotiated word limit and contain no coordinate protocol.
- **LSB-AC-06:** invalid or oversized hints reject/fallback deterministically.
- **LSB-AC-07:** cop belief is normalized, barrier-aware, and role-correct.
- **LSB-AC-08:** scent and language updates are repeatable and handle zero-weight evidence safely.
- **LSB-AC-09:** strategy receives belief through a typed boundary and still passes actions through Base Logic.
- **LSB-AC-10:** template mode consumes zero provider tokens and provider failures do not stop gameplay.

## Authority matrix

| Source | Owned requirements |
|---|---|
| Appendix E 23 | pre-game cryptographic locking is deferred to Stage 6; Stage 4 produces lockable deterministic model data |
| Appendix E 25-27 | LLM separation, natural-language-only communication, no direct numeric locations |
| Annex F Table 14 | negotiable area and 15-word default |
| Annex F Table 16 | fixed scent 0.9, 0.10, 5x5 |
| ADR-004 | exact shared arithmetic and cop-specific belief |

## Non-goals

Commit-Reveal locking, public tunnels, Gmail, GUI, replay, RL training, and provider-specific private credentials.

## Live-match composition extension

For an accepted movement/STAY turn, composition order is previous-field decay, new emission, maximum/clipping, scent observation, optional validated qualitative hint, scent-first then language belief update, and next-turn strategy input. Rejected actions and cop barrier actions do not emit movement scent. Versioned scent/hint message contracts and cross-peer ordering tests remain pending.
