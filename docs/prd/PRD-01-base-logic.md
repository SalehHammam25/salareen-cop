# PRD-01: Base Logic

**Status:** Owner-approved requirements; implementation not started
**Specification:** 3.0.0
**Decision:** ADR-001

## Purpose

Define the deterministic local physics shared by both peers while preserving the cop's exclusive barrier authority. Networking, strategy, language, scent, cryptography, GUI, and reporting are excluded.

## Mandatory requirements

### Configuration and state

- Exactly two roles exist: cop and thief.
- Shared `config/game.json` is validated before state creation; rejection creates no partial state.
- Board size defaults to 7x7 and is a minimum.
- Coordinate origin, starting index, and both starting positions are negotiable and must match between peers.
- State records positions, permanent barriers, placed-barrier count, valid-step count, active role, terminal outcome, and score.
- `max_moves` and `survival_threshold` each default to minimum 35 and, by ADR-001, must be equal.
- Identical accepted configuration and action sequences produce identical results.

### Actions and barriers

- One active role performs exactly one action: N, S, E, W, STAY, or (cop only) barrier placement.
- Movement is exactly one orthogonal cell; diagonal and off-board movement reject without mutation.
- Neither peer may enter a barrier.
- Barrier placement replaces cop movement, is limited to the cop cell or one orthogonally adjacent cell, and must be declared truthfully.
- Barrier quota defaults to minimum 14; barriers are permanent and impassable.
- Own-cell placement is allowed. Current cop occupancy is grandfathered until departure; re-entry is forbidden.
- Rejected actions neither advance the turn nor consume resources.

### Capture and outcomes

- Coordinate overlap, barrier-on-thief, and trapped-thief paths all require a valid local Capture Claim.
- A trapped thief has no legal orthogonal destination; STAY is not an escape.
- Capture is evaluated before survival.
- Survival occurs at the equal configured threshold/ceiling without capture.
- Technical loss is representable but its detection belongs to later stages.
- Terminal state rejects further mutation.

### Scoring

Fixed score pairs are: capture (cop 20, thief 5), survival (cop 5, thief 10), technical loss (0, 0). Fixed series tie score 2 is outside Stage 1.

## Acceptance criteria

- **BL-AC-01:** valid configuration creates complete deterministic state.
- **BL-AC-02:** malformed, incomplete, below-minimum, inconsistent, or unequal ceiling/threshold configuration rejects atomically.
- **BL-AC-03:** N/S/E/W and STAY behave deterministically.
- **BL-AC-04:** diagonal, off-board, barrier-collision, wrong-role, combined, and terminal actions reject without mutation.
- **BL-AC-05:** valid cop barriers replace movement, persist, consume quota once, and record exact location.
- **BL-AC-06:** invalid location, duplicate, thief placement, and exhausted quota reject atomically.
- **BL-AC-07:** own-cell grandfathering permits immediate occupancy and forbids later re-entry.
- **BL-AC-08:** each capture path requires and validates the correct common claim.
- **BL-AC-09:** STAY cannot avoid trapped-thief capture.
- **BL-AC-10:** capture wins transition-order priority over survival.
- **BL-AC-11:** each terminal outcome maps to its exact fixed score pair.
- **BL-AC-12:** repeated complete executions are equal.

## Authority matrix

| Source | Owned requirements |
|---|---|
| Appendix E 11-16 | identical configuration, movement, no diagonal, truthful barrier declaration/location |
| Appendix E 21-22 | truthful Capture Claim behavior |
| Appendix E 46-48 | barrier/trapped capture and fixed scoring |
| Annex F Table 13 | board/coordinate/start values and statuses |
| Annex F Table 15 | movement, barrier 14 minimum, ceiling/threshold 35 minimum |
| Annex F Table 17 | fixed score values |
| ADR-001 | formerly ambiguous Stage 1 transitions |

## Non-goals

FastMCP, public endpoints, strategy selection, scent, language providers, Commit-Reveal, watchdog detection, GUI, replay, Gmail, and league aggregation.
