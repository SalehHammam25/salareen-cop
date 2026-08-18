# TODO-03: Blind Cop Strategy

**Status:** Implementation complete on stacked branch; Pull Request and merge pending
**Related PRD:** `../prd/PRD-03-blind-strategy.md`
**Related PLAN:** `../PLAN.md`

Each item is meaningful implementation or verification work. IDs are stable and unique. Authority ownership is defined in PRD-03.

## Governance

- [x] **STR-001** Approve PRD-03 and ADR-003. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-002** Map strategy acceptance criteria. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-003** Record no-RL decision. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-004** Record role-specific cop boundary. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-005** Create future Stage 3 branch. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Interfaces

- [x] **STR-006** Define immutable strategy snapshot. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-007** Define typed action proposal. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-008** Define typed decision success. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-009** Define typed failure reasons. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-010** Keep strategy unable to mutate state. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Pursuit target

- [x] **STR-011** Accept permitted estimated target only. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-012** Reject target outside board. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-013** Reject target on impossible cell. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-014** Avoid opponent private state. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-015** Test target input repeatability. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Path search

- [x] **STR-016** Compute legal orthogonal paths. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-017** Respect permanent barriers. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-018** Respect board boundaries. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-019** Bound search by board size. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-020** Return deterministic unreachable result. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Move choice

- [x] **STR-021** Prefer reduced shortest distance. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-022** Include STAY only when appropriate. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-023** Document stable movement tie order. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-024** Avoid illegal direct displacement. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-025** Test symmetric tie scenarios. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Barrier candidates

- [x] **STR-026** Generate only cop-relative legal cells. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-027** Respect remaining quota. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-028** Evaluate thief escape-route reduction. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-029** Evaluate cop reachability cost. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-030** Document stable barrier tie order. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Barrier safety

- [x] **STR-031** Avoid duplicate barrier proposals. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-032** Avoid off-board proposals. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-033** Honor grandfathered occupancy rule. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-034** Avoid needless self-containment when safer tie exists. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-035** Test constrained corridor choices. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Validation gateway

- [x] **STR-036** Revalidate every proposal through Base Logic. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-037** Preserve state during proposal validation. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-038** Reject illegal proposal deterministically. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-039** Apply only accepted proposal later. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-040** Test validation gateway isolation. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Fallback

- [x] **STR-041** Define deterministic default policy. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-042** Fallback on plugin import error. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-043** Fallback on plugin exception. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-044** Fallback on malformed proposal. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-045** Revalidate fallback through Base Logic. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Plugins

- [x] **STR-046** Define optional class reference syntax. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-047** Reject missing class. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-048** Reject wrong interface. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-049** Reject constructor failure. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-050** Keep private selection outside shared config. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Boundaries

- [x] **STR-051** Prohibit LLM movement selection. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-052** Prohibit network dependency. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-053** Prohibit scent dependency. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-054** Prohibit thief strategy reuse. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-055** Prohibit direct state mutation. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Tests

- [x] **STR-056** Test open-board pursuit. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-057** Test barrier detour pursuit. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-058** Test unreachable target. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-059** Test deterministic ties. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-060** Test adversarial plugin failures. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Delivery

- [x] **STR-061** Run focused and complete tests. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-062** Run lint and line-length gates. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-063** Review role-specific behavior. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [x] **STR-064** Record verification evidence. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]
- [ ] **STR-065** Merge only through verified Pull Request. [Authority: PRD-03; PLAN Stage 3; Appendix E and Annex F via the PRD authority matrix]

## Completion gate

Stage 3 completes only after every applicable task is finished, acceptance criteria have tests, evidence records exact results, adversarial defects are corrected, and a Pull Request is approved and merged.
