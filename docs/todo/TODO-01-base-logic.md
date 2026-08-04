# TODO 01 — Base Logic

**Status:** Not started
**Repository:** salareen-cop
**Related PRD:** `../prd/PRD-01-base-logic.md`
**Related PLAN:** `../PLAN.md`

## Goal

This checklist prepares the deterministic, local, single-process Base Logic foundation for the cop peer.

Networking, FastMCP, strategy, LLMs, cryptography, GUI, replay, and reporting are not part of this TODO.

Implementation is blocked until PRD-01 receives formal approval and PRD ↔ PLAN ↔ TODO coverage is verified.

## Lifecycle and Review Preconditions

- [ ] Review every mandatory requirement and acceptance criterion in PRD-01
- [ ] Preserve all Annex F numerical values and statuses
- [ ] Keep all five PRD Open Questions unresolved
- [ ] Confirm no implementation depends on an unresolved question without documenting the blocker
- [ ] Confirm PRD-01 formal approval before implementation begins
- [ ] Review the merged PLAN
- [ ] Verify every PRD mandatory requirement maps to at least one PLAN item and TODO task
- [ ] Verify every PRD acceptance criterion maps to planned tests
- [ ] Confirm no implementation begins before PRD, PLAN, and TODO review
- [ ] Work on a dedicated implementation branch
- [ ] Preserve meaningful Git history
- [ ] Use Pull Requests and merge only when stable

## Environment and Project Foundation

- [ ] Initialize the Python project using `uv`
- [ ] Record the exact `uv` initialization command
- [ ] Establish separation between source code and unit tests
- [ ] Ensure local environments and caches are ignored by Git
- [ ] Verify credentials, tokens, secrets, and private keys are excluded
- [ ] Establish an automated or repeatable check that every Python file is at most 150 lines
- [ ] Split files by responsibility whenever the limit would be exceeded
- [ ] Confirm project actions and commands are performed through the terminal
- [ ] Record exact commands and results during implementation

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
- [ ] Validate agreed numerical values and statuses before creating the initial state
- [ ] Reject invalid initial state explicitly
- [ ] Ensure failed initialization does not create partial state
- [ ] Verify identical input produces identical initial state
- [ ] Keep configuration integration blocked until the related Open Question is decided

## Movement Rules

- [ ] Plan enforcement of one action per active turn
- [ ] Plan enforcement of one-cell orthogonal movement
- [ ] Plan support for staying in place
- [ ] Plan deterministic rejection of diagonal movement
- [ ] Plan deterministic rejection of movement into a barrier
- [ ] Leave off-grid movement behavior blocked as an unresolved specification question
- [ ] Define explicit success and rejection outcomes without inventing their implementation form
- [ ] Verify rejected moves do not mutate any game state
- [ ] Verify the active turn is unchanged or changed only according to a later documented decision
- [ ] Keep all off-grid implementation and tests blocked until the Open Question is resolved
- [ ] Add boundary tests after a documented decision exists

## Barrier Rules

- [ ] Plan restricting barrier placement to the cop only
- [ ] Plan making barrier placement replace movement for that turn
- [ ] Plan validating placement on the cop's current cell or one orthogonally adjacent cell
- [ ] Plan enforcing the barrier quota
- [ ] Plan making barriers permanent for the rest of the episode
- [ ] Plan preventing both agents from entering barrier cells
- [ ] Plan recording the exact declared barrier location
- [ ] Keep the cop-on-new-barrier occupancy issue unresolved
- [ ] Reject placement by the thief
- [ ] Reject placement outside the permitted cop-relative cells
- [ ] Reject placement beyond the quota
- [ ] Verify rejected placement does not mutate state or consume quota
- [ ] Verify stored barrier count matches the permanent barrier set
- [ ] Keep cop occupancy on a newly blocked current cell unresolved and blocked

## Capture and End Conditions

- [ ] Plan coordinate-overlap capture with Capture Claim
- [ ] Plan barrier-on-thief-cell capture
- [ ] Plan trapped-thief capture
- [ ] Plan survival after the configured valid-step threshold
- [ ] Plan recognition of technical-loss as an outcome, without implementing crash, timeout, or cryptographic detection
- [ ] Keep the relationship between move ceiling and survival threshold unresolved
- [ ] Keep Capture Claim requirements for non-overlap capture unresolved
- [ ] Define deterministic precedence if multiple documented end conditions are simultaneously true, but keep this blocked unless the specification already determines it
- [ ] Prevent state-changing actions after the episode is terminal
- [ ] Verify repeated end-condition evaluation returns the same result
- [ ] Keep move-ceiling behavior blocked until its relationship with survival is decided
- [ ] Keep Capture Claim behavior for non-overlap capture blocked

## Scoring

- [ ] Plan returning the fixed Capture score pair: cop 20, thief 5
- [ ] Plan returning the fixed Survival score pair: cop 5, thief 10
- [ ] Plan returning the fixed Technical loss score pair: cop 0, thief 0
- [ ] Note that the tie score (2) is outside the per-episode Base Logic implementation
- [ ] Ensure every supported terminal outcome maps to exactly one fixed score pair
- [ ] Reject or expose unsupported outcomes explicitly
- [ ] Ensure repeated scoring of the same final outcome is deterministic
- [ ] Verify the league tie score is not applied inside a single episode

## Deterministic Validation

- [ ] Plan ensuring game legality is decided only by deterministic code
- [ ] Plan ensuring an LLM cannot approve moves, barriers, capture, or scoring
- [ ] Plan ensuring the same initial state and action sequence always produce the same result
- [ ] Plan ensuring invalid actions do not silently change state
- [ ] Ensure no LLM call exists in Base Logic
- [ ] Ensure invalid input fails explicitly
- [ ] Ensure no rejected action silently mutates state
- [ ] Verify the same initial state and action sequence always produce identical states, outcome, and scores
- [ ] Verify deterministic behavior across repeated test runs

## Unit-Test Planning

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
- [ ] Plan a test for invalid initial state
- [ ] Plan a test for deterministic initial-state creation
- [ ] Plan a test for the thief attempting barrier placement
- [ ] Plan a test for invalid barrier location
- [ ] Plan a test confirming no quota consumption after rejected placement
- [ ] Plan a test confirming no state mutation after every rejected-action category
- [ ] Plan a test for actions attempted after an episode ends
- [ ] Plan a test for repeated end-condition evaluation
- [ ] Plan a test for repeated scoring
- [ ] Plan a test for unsupported outcome handling
- [ ] Plan a test for multiple complete repeated executions
- [ ] Plan the future off-grid tests after a documented decision

Test code is not written at this stage.

## Completion Checklist

- [ ] Confirm all PRD-01 acceptance criteria are covered by planned tests
- [ ] Confirm no unresolved question was answered through implementation assumptions
- [ ] Complete implementation and tests later on a dedicated implementation branch
- [ ] Record exact test commands and results after implementation
- [ ] Review PRD-01 and TODO-01 before Base Logic is declared complete

## Verification and Traceability

- [ ] Create a PRD acceptance-criterion to test-coverage checklist
- [ ] Create a PRD requirement to PLAN/TODO coverage checklist
- [ ] Run the complete unit-test suite later
- [ ] Run the 150-line check later
- [ ] Record exact commands, exit codes, and results
- [ ] Review the final diff for scope violations
- [ ] Confirm no later-stage functionality was introduced
- [ ] Open and review a Pull Request
- [ ] Merge only after successful verification
- [ ] Synchronize and clean main after merge

## Project-Wide TODO Contribution

This TODO contributes meaningful Base Logic tasks toward the course expectation of at least 500 meaningful tasks across all project TODO documents. No artificial padding is allowed. Later TODO documents must be expanded when their PRDs and PLAN sections are prepared.

## Blocked / Open Questions

- [ ] What exact response is required when a move targets a coordinate outside the board?
  - [ ] Record a documented decision before affected implementation begins
  - [ ] Update PRD, PLAN, TODO, and tests consistently after the decision
- [ ] What is the precise relationship between the move ceiling (תקרת הצעדים) and the survival threshold (סף ההישרדות) if negotiated to different values?
  - [ ] Record a documented decision before affected implementation begins
  - [ ] Update PRD, PLAN, TODO, and tests consistently after the decision
- [ ] Do barrier-on-thief-cell capture and trapped-thief capture require the same Capture Claim and later cryptographic truth-verification flow as coordinate-overlap capture?
  - [ ] Record a documented decision before affected implementation begins
  - [ ] Update PRD, PLAN, TODO, and tests consistently after the decision
- [ ] When the cop places a barrier on the cell it currently occupies, how is its immediate occupancy handled after that cell becomes impassable to both agents?
  - [ ] Record a documented decision before affected implementation begins
  - [ ] Update PRD, PLAN, TODO, and tests consistently after the decision
- [ ] Is `config/game.json` used directly during Base Logic, or introduced only after the configuration layer is implemented?
  - [ ] Record a documented decision before affected implementation begins
  - [ ] Update PRD, PLAN, TODO, and tests consistently after the decision
