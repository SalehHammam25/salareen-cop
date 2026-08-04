# TODO 01 — Base Logic

**Status:** Not started
**Repository:** salareen-cop
**Related PRD:** `../prd/PRD-01-base-logic.md`

## Goal

This checklist prepares the deterministic, local, single-process Base Logic foundation for the cop peer.

Networking, FastMCP, strategy, LLMs, cryptography, GUI, replay, and reporting are not part of this TODO.

## Preconditions

- [ ] Review every mandatory requirement and acceptance criterion in PRD-01
- [ ] Preserve all Annex F numerical values and statuses
- [ ] Keep all five PRD Open Questions unresolved
- [ ] Confirm no implementation depends on an unresolved question without documenting the blocker

## Shared Game Model

- [ ] Define the representation of exactly two agent roles: cop and thief
- [ ] Define the representation of board dimensions
- [ ] Define the representation of `(row, col)` coordinates
- [ ] Define the representation of coordinate origin and starting index
- [ ] Define the representation of starting positions
- [ ] Define the representation of current cop and thief positions
- [ ] Define the representation of permanent barriers
- [ ] Define the representation of barrier count and quota
- [ ] Define the representation of valid-step count
- [ ] Define the representation of episode status
- [ ] Define the representation of final outcome and score pair

## Movement Rules

- [ ] Plan enforcement of one action per active turn
- [ ] Plan enforcement of one-cell orthogonal movement
- [ ] Plan support for staying in place
- [ ] Plan deterministic rejection of diagonal movement
- [ ] Plan deterministic rejection of movement into a barrier
- [ ] Leave off-grid movement behavior blocked as an unresolved specification question

## Barrier Rules

- [ ] Plan restricting barrier placement to the cop only
- [ ] Plan making barrier placement replace movement for that turn
- [ ] Plan validating placement on the cop's current cell or one orthogonally adjacent cell
- [ ] Plan enforcing the barrier quota
- [ ] Plan making barriers permanent for the rest of the episode
- [ ] Plan preventing both agents from entering barrier cells
- [ ] Plan recording the exact declared barrier location
- [ ] Keep the cop-on-new-barrier occupancy issue unresolved

## Capture and End Conditions

- [ ] Plan coordinate-overlap capture with Capture Claim
- [ ] Plan barrier-on-thief-cell capture
- [ ] Plan trapped-thief capture
- [ ] Plan survival after the configured valid-step threshold
- [ ] Plan recognition of technical-loss as an outcome, without implementing crash, timeout, or cryptographic detection
- [ ] Keep the relationship between move ceiling and survival threshold unresolved
- [ ] Keep Capture Claim requirements for non-overlap capture unresolved

## Scoring

- [ ] Plan returning the fixed Capture score pair: cop 20, thief 5
- [ ] Plan returning the fixed Survival score pair: cop 5, thief 10
- [ ] Plan returning the fixed Technical loss score pair: cop 0, thief 0
- [ ] Note that the tie score (2) is outside the per-episode Base Logic implementation

## Deterministic Validation

- [ ] Plan ensuring game legality is decided only by deterministic code
- [ ] Plan ensuring an LLM cannot approve moves, barriers, capture, or scoring
- [ ] Plan ensuring the same initial state and action sequence always produce the same result
- [ ] Plan ensuring invalid actions do not silently change state

## Tests

- [ ] Plan tests for every legal orthogonal direction
- [ ] Plan a test for staying in place
- [ ] Plan a test for diagonal rejection
- [ ] Plan a test for barrier collision rejection
- [ ] Plan a test for valid cop barrier placement
- [ ] Plan a test for invalid barrier placement
- [ ] Plan a test for barrier quota enforcement
- [ ] Plan a test for barrier permanence
- [ ] Plan a test for coordinate-overlap capture
- [ ] Plan a test for barrier-on-thief capture
- [ ] Plan a test for trapped-thief capture
- [ ] Plan a test for the survival threshold
- [ ] Plan tests for all three score pairs
- [ ] Plan a test for deterministic repeated execution
- [ ] Plan a test confirming no state mutation after a rejected action

Test code is not written at this stage.

## Completion Checklist

- [ ] Confirm all PRD-01 acceptance criteria are covered by planned tests
- [ ] Confirm no unresolved question was answered through implementation assumptions
- [ ] Complete implementation and tests later on a dedicated implementation branch
- [ ] Record exact test commands and results after implementation
- [ ] Review PRD-01 and TODO-01 before Base Logic is declared complete

## Blocked / Open Questions

- [ ] What exact response is required when a move targets a coordinate outside the board?
- [ ] What is the precise relationship between the move ceiling (תקרת הצעדים) and the survival threshold (סף ההישרדות) if negotiated to different values?
- [ ] Do barrier-on-thief-cell capture and trapped-thief capture require the same Capture Claim and later cryptographic truth-verification flow as coordinate-overlap capture?
- [ ] When the cop places a barrier on the cell it currently occupies, how is its immediate occupancy handled after that cell becomes impassable to both agents?
- [ ] Is `config/game.json` used directly during Base Logic, or introduced only after the configuration layer is implemented?
