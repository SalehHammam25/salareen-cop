# TODO-04: Language, Scent, and Belief

**Status:** Implementation complete on stacked branch; Pull Request and merge pending
**Related PRD:** `../prd/PRD-04-language-and-scent.md`
**Related PLAN:** `../PLAN.md`

Each item is meaningful implementation or verification work. IDs are stable and unique. Authority ownership is defined in PRD-04.

## Governance

- [x] **LSB-001** Approve PRD-04 and ADR-004. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-002** Map Appendix E rules 23 and 25-27. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-003** Verify Annex F Tables 14 and 16. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-004** Record Stage 6 locking deferral. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-005** Create future Stage 4 branch. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Scent config

- [x] **LSB-006** Fix center intensity at 0.9. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-007** Fix decay at 0.10. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-008** Fix field size at 5x5. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-009** Reject overrides of fixed values. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-010** Match thief fixture schema. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Kernel

- [x] **LSB-011** Define exact radial kernel values. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-012** Use deterministic numeric representation. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-013** Clip negative intensity at zero. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-014** Do not renormalize at edges. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-015** Test center edge and corner kernels. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Emission

- [x] **LSB-016** Emit for movement turns. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-017** Emit for STAY turns. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-018** Apply identical per-role source rules. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-019** Aggregate overlapping deposits deterministically. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-020** Test repeated emission behavior. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Decay

- [x] **LSB-021** Apply decay once per agreed full turn. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-022** Use exact operation ordering. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-023** Prevent floating-order divergence. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-024** Remove numerical underflow consistently. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-025** Test long decay sequence. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Transition order

- [x] **LSB-026** Document decay position in turn. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-027** Document movement position in turn. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-028** Document emission position in turn. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-029** Document observation and belief update order. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-030** Match thief transition fixture exactly. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Hints

- [x] **LSB-031** Define free-form natural-language hint. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-032** Enforce negotiated default 15 words. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-033** Reject direct numeric coordinate protocol. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-034** Validate template output. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-035** Return typed invalid-hint result. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Providers

- [x] **LSB-036** Implement future template provider boundary. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-037** Keep template mode zero-token. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-038** Isolate optional provider adapters. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-039** Fallback on provider failure. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-040** Never expose provider secrets. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Accounting

- [x] **LSB-041** Count provider input and output consistently. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-042** Record per-step token use. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-043** Record per-series token use. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-044** Keep accounting independent of actions. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-045** Test deterministic zero-token path. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Belief prior

- [x] **LSB-046** Create cop belief over thief cells. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-047** Exclude barriers and impossible cells. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-048** Normalize probability mass. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-049** Use deterministic numeric arithmetic. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-050** Test reproducible prior. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Belief updates

- [x] **LSB-051** Update from thief scent. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-052** Update from language reliability. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-053** Handle contradictory evidence. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-054** Fallback on zero total weight. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-055** Preserve normalized valid belief. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Strategy integration

- [x] **LSB-056** Pass belief through typed snapshot. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-057** Keep action choice in Stage 3 policy. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-058** Revalidate resulting proposal. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-059** Prevent provider text from selecting action. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-060** Test role-correct pursuit use. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Delivery

- [x] **LSB-061** Run cross-peer scent fixtures. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-062** Run focused and complete tests. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-063** Scan for coordinate protocol and secrets. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [x] **LSB-064** Record verification evidence. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]
- [ ] **LSB-065** Merge only through verified Pull Request. [Authority: PRD-04; PLAN Stage 4; Appendix E and Annex F via the PRD authority matrix]

## Completion gate

Stage 4 completes only after every applicable task is finished, acceptance criteria have tests, evidence records exact results, adversarial defects are corrected, and a Pull Request is approved and merged.

## Live-match composition backlog

- [ ] **LM-LSB-001** Connect accepted movement/STAY to scent decay/emission exactly once; exclude rejected and barrier actions.
- [ ] **LM-LSB-002** Implement versioned scent observation and language hint transport adapters.
- [ ] **LM-LSB-003** Apply scent before language evidence and expose the result only to the next cop strategy invocation.
- [ ] **LM-LSB-004** Test coordinate prohibition, provider fallback and token accounting inside complete turns.
- [ ] **LM-LSB-005** Add byte-identical Stage 4 turn fixtures and cross-process ordering tests.
