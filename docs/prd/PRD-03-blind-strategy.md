# PRD-03: Blind Cop Strategy

**Status:** Owner-approved requirements; implementation not started
**Specification:** 3.0.0
**Decision:** ADR-003

## Purpose

Choose legal cop movements and barriers deterministically using only permitted local state and an estimated target, before language and scent exist.

## Mandatory requirements

- Strategy is isolated from Base Logic and cannot mutate authoritative state.
- Input is an immutable snapshot; output is a typed move or barrier proposal.
- Every proposal is revalidated through Base Logic before application.
- The default cop policy pursues the target rather than copying thief escape behavior.
- Orthogonal shortest-path distance and barriers guide pursuit.
- Barrier proposals may contain escape routes but must consider cop reachability, quota, and self-containment risk.
- Deterministic action and barrier tie orders are documented and stable.
- Invalid plugin references, exceptions, malformed results, and illegal proposals produce typed deterministic fallback.
- Fallback itself must pass Base Logic validation.
- Strategy receives no opponent private state and no omniscient board.
- LLMs do not select or validate movement.
- Reinforcement learning is not required and is excluded absent a later explicit decision.

## Acceptance criteria

- **STR-AC-01:** open-board pursuit reduces shortest legal distance when possible.
- **STR-AC-02:** pathfinding respects board edges and permanent barriers.
- **STR-AC-03:** cop action ordering is deterministic across processes.
- **STR-AC-04:** legal containment barriers can be proposed within quota.
- **STR-AC-05:** policy avoids barriers that immediately eliminate every useful cop route when a safer equal option exists.
- **STR-AC-06:** every proposal passes through Base Logic and invalid proposals do not mutate state.
- **STR-AC-07:** plugin failure, exception, malformed output, and illegal output yield typed fallback.
- **STR-AC-08:** fallback is deterministic and legal.
- **STR-AC-09:** tests prove no thief private-state, LLM, network, or Stage 4 dependency.
- **STR-AC-10:** repeated snapshots produce repeated proposals.

## Authority matrix

| Source | Owned requirements |
|---|---|
| Chapter 6 | separate strategy module; deterministic spatial authority |
| Appendix E 25 | recommendation against LLM movement is adopted as project policy |
| Appendix E 13-16 | all selected actions remain subject to mandatory physics |
| Annex F Tables 13/15 | strategy consumes, but cannot weaken, agreed board/action limits |
| ADR-003 | cop-specific pursuit/barrier boundary and exclusions |

## Non-goals

Scent, belief inference from evidence, natural-language text, providers, network transport, RL training, cryptography, GUI, and reporting.
