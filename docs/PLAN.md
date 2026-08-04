# Project Implementation Plan

**Status:** Active
**Repository:** salareen-cop
**Current stage:** Stage 1 — Base Logic
**Implementation:** Not started

## Development Lifecycle

The required workflow is:

Idea → PRD → PLAN → TODO → Verify → Execute → Push to GitHub

- Implementation must not begin until the related PRD, PLAN, and TODO have been reviewed.
- Every PRD requirement must be traceable to PLAN work and TODO tasks.
- Each meaningful change is developed on a branch, tested, reviewed through a Pull Request, and merged into main only when stable.
- Git history must show continuous, meaningful development.
- The project TODO files should eventually contain at least 500 meaningful tasks in total, with 800–1000 presented by the course as an ideal level of decomposition.
- Tasks must be genuine work items, not artificial padding.

## Course Engineering Constraints

- Project work is performed through terminal commands.
- Claude CLI is the preferred agent interface.
- Python environment and dependency management use `uv`.
- Unit tests are required.
- Every Python file must remain at or below 150 lines, with no exceptions; longer files must be split by responsibility.
- Deterministic rules must remain separate from LLM behavior.
- No secrets, credentials, tokens, or private keys may ever be committed.
- Exact commands and test results must be recorded during implementation.
- Invalid input must fail explicitly and must not silently mutate state.

Project actions are performed through the terminal; this does not prohibit the use of VS Code itself.

## Stage Order

1. Base Logic
2. Basic MCP Infrastructure
3. Blind Strategy
4. Language and Scent
5. Cloud Exposure and Tunneling
6. Security and Cryptography
7. Reporting and Visualization Shell

This order follows Chapter 10's recommended staged approach. It is **recommended, not mandatory**.

Later stages must not be implemented before their prerequisites work end-to-end.

## Stage 1 — Base Logic

### Objective

Build and verify the deterministic, local, single-process game-physics foundation for the cop peer.

It must cover:

- board and coordinate state;
- legal movement;
- barriers;
- capture and survival;
- technical-loss outcome representation;
- fixed per-episode scoring;
- deterministic repeatability.

Networking, FastMCP, strategy, LLMs, cryptography, GUI, replay, and reporting are excluded.

### Inputs

- `docs/prd/PRD-01-base-logic.md`
- Annex F numerical values and statuses already recorded in PRD-01
- the five unresolved PRD Open Questions
- `docs/todo/TODO-01-base-logic.md`, currently prepared on its dedicated Draft Pull Request branch and awaiting revision against this PLAN

PRD-01 is merged but still marked Draft, so formal approval must be completed before implementation begins.

### Implementation Sequence

The implementation strategy follows this dependency order. No filenames, classes, functions, or APIs are specified here.

1. Environment and project foundation
   - initialize the Python project with `uv`;
   - establish source and unit-test separation;
   - establish checks for the 150-line Python-file limit;
   - confirm secrets and local environments are excluded from Git.

2. Shared deterministic game state
   - represent both agent roles;
   - board dimensions and coordinate conventions;
   - starting and current positions;
   - barriers and barrier quota;
   - valid-step count;
   - episode status;
   - outcome and score pair.

3. Movement validation
   - orthogonal one-cell movement;
   - staying in place;
   - diagonal rejection;
   - barrier collision rejection;
   - no state mutation after rejection.

4. Barrier behavior
   - only the cop may place barriers;
   - placement replaces movement;
   - location validation;
   - quota enforcement;
   - permanence and impassability;
   - exact declared location storage.

5. End-condition evaluation
   - coordinate-overlap capture with Capture Claim;
   - barrier-on-thief-cell capture;
   - trapped-thief capture;
   - survival threshold;
   - representation of technical loss without implementing later-stage detection mechanisms.

6. Scoring
   - Capture: cop 20, thief 5;
   - Survival: cop 5, thief 10;
   - Technical loss: cop 0, thief 0;
   - tie score 2 remains outside per-episode Base Logic.

7. Unit-test implementation
   - cover every PRD-01 acceptance criterion;
   - cover legal movement, explicitly specified illegal actions, quota, capture, survival, scoring, and determinism behavior;
   - off-grid boundary behavior remains blocked from implementation and testing until its Open Question receives a documented decision;
   - after that decision, add the corresponding boundary tests before Base Logic can be completed;
   - verify rejected actions do not mutate state.

8. Verification and review
   - run the complete unit-test suite;
   - run the 150-line limit check;
   - review PRD-to-PLAN-to-TODO traceability;
   - record exact commands and results;
   - open a Pull Request;
   - merge only after review and successful verification.

### Open-Question Handling

The five unresolved PRD questions:

1. off-grid movement response;
2. relationship between move ceiling and survival threshold;
3. Capture Claim requirements for barrier/trapped capture;
4. cop occupancy after placing a barrier on its own cell;
5. when `config/game.json` enters the Base Logic lifecycle.

For each one:

- it must not be silently answered through implementation;
- affected implementation work remains blocked until a documented decision is made;
- the decision must be recorded before the relevant TODO item is executed.

These questions are not resolved here.

### Verification Gate

Base Logic may be declared complete only when:

- PRD-01 has formal approval;
- every acceptance criterion maps to at least one unit test;
- all tests pass;
- all Python files satisfy the 150-line limit;
- execution is deterministic;
- no unresolved question was answered by assumption;
- no networking, strategy, LLM, cryptography, GUI, replay, or reporting work was introduced;
- any behavior previously blocked by an Open Question has a documented decision and corresponding tests before completion;
- the Pull Request is reviewed and merged;
- main is clean and synchronized with origin/main.

## Later-Stage Planning

For Stages 2–7:

- their PRD must be completed and approved first;
- their section in PLAN must then be expanded;
- their detailed TODO must then be prepared and verified;
- implementation begins only after that cycle is complete.

No technical details beyond this have been extracted from their PRDs yet.

## Planning Snapshot

This section records the repository state while this PLAN was prepared and is not a permanent runtime requirement.

- PRD-01 is merged into main.
- PRD-01 is still labeled Draft and requires a later approval update.
- The TODO-01 branch and Draft Pull Request exist but must not be merged yet.
- No implementation code exists.
- This PLAN was prepared on branch `docs/plan-01-base-logic`.

## Next Documentation Steps

1. Review the expanded PLAN.
2. Commit and push the PLAN branch.
3. Open and review the PLAN Pull Request.
4. Merge PLAN into main.
5. Update the TODO-01 branch with main.
6. Revise TODO-01 so it follows the approved PLAN and course constraints.
7. Verify PRD ↔ PLAN ↔ TODO coverage.
8. Merge TODO-01.
9. Formally approve PRD-01 before implementation.
10. Create a dedicated Base Logic implementation branch.
