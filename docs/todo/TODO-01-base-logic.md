# TODO-01: Base Logic

**Status:** Execution-ready documentation; implementation not started
**Related PRD:** `../prd/PRD-01-base-logic.md`
**Related PLAN:** `../PLAN.md`

Each item is meaningful implementation or verification work. IDs are stable and unique. Authority ownership is defined in PRD-01.

## Governance

- [ ] **BL-001** Confirm PRD-01 owner approval is recorded. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-002** Review ADR-001 decisions against PRD-01. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-003** Map every PRD acceptance criterion to tasks. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-004** Map Appendix E rules 11-16 to owners. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-005** Map Appendix E rules 21-22 to owners. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-006** Map Appendix E rules 46-48 to owners. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-007** Verify Annex F Tables 13, 15, and 17 are transcribed exactly. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-008** Record Stage 1 non-goals before implementation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-009** Create the future focused implementation branch. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-010** Record the future Pull Request and verification gate. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Foundation

- [ ] **BL-011** Initialize the future Python project with uv. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-012** Create separate source and test roots. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-013** Define the future package name for the cop peer. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-014** Add a repeatable 150-line Python-file check. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-015** Add deterministic test configuration. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-016** Add lint configuration without weakening rules. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-017** Protect virtual environments and caches in gitignore. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-018** Protect credentials and private configuration in gitignore. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-019** Record exact setup commands in verification evidence. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-020** Prove foundation imports in a clean environment. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Config schema

- [ ] **BL-021** Define strict shared JSON top-level sections. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-022** Define board and agent schema fields. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-023** Define movement and barrier schema fields. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-024** Define scoring schema fields. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-025** Reject unknown shared configuration fields. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-026** Reject missing mandatory configuration fields. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-027** Reject Boolean values where integers are required. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-028** Reject malformed UTF-8 and duplicate JSON keys. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-029** Return ordered typed configuration issues. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-030** Keep private local settings outside shared JSON. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Config values

- [ ] **BL-031** Enforce grid size minimum 7. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-032** Enforce exactly two agents. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-033** Validate negotiable coordinate origin. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-034** Validate negotiable starting index. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-035** Validate both negotiated starting positions. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-036** Enforce barrier quota minimum 14. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-037** Enforce max moves minimum 35. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-038** Enforce survival threshold minimum 35. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-039** Enforce equal max moves and survival threshold. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-040** Enforce fixed score values and reject overrides. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## State model

- [ ] **BL-041** Define immutable coordinate representation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-042** Define immutable board representation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-043** Define explicit cop and thief roles. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-044** Define immutable positions aggregate. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-045** Define permanent barrier collection. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-046** Define placed-barrier count. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-047** Define valid-step count. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-048** Define active-role state. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-049** Define terminal outcome model. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-050** Define score-pair model. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## State creation

- [ ] **BL-051** Build initial state only from accepted configuration. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-052** Reject starting positions outside the board. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-053** Reject duplicate starting positions when configuration forbids overlap. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-054** Reject starting positions on barriers. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-055** Reject barriers outside the board. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-056** Reject barrier count above quota. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-057** Reject inconsistent stored barrier count. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-058** Prevent partial state on failed construction. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-059** Produce equal states from equal inputs. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-060** Test state hashing or equality deterministically. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Movement model

- [ ] **BL-061** Define N movement delta. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-062** Define S movement delta. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-063** Define E movement delta. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-064** Define W movement delta. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-065** Define STAY zero delta. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-066** Reject diagonal displacement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-067** Reject multi-cell displacement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-068** Reject off-board destination. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-069** Reject barrier destination. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-070** Reject movement by the inactive role. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Movement transitions

- [ ] **BL-071** Apply one legal movement atomically. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-072** Advance valid-step count once after accepted movement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-073** Advance active role once after accepted movement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-074** Keep state identity on rejected movement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-075** Preserve barrier collection during movement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-076** Preserve barrier quota during movement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-077** Reject combined movement and barrier action. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-078** Reject unknown action types. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-079** Reject all actions after terminal outcome. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-080** Test repeated movement sequence equality. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Barrier validation

- [ ] **BL-081** Restrict barrier actions to the cop. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-082** Allow placement on the cop current cell. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-083** Allow placement on each orthogonally adjacent cell. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-084** Reject non-adjacent placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-085** Reject off-board placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-086** Reject duplicate barrier placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-087** Reject placement after quota exhaustion. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-088** Reject thief barrier placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-089** Reject combined placement and movement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-090** Return typed barrier rejection reasons. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Barrier transitions

- [ ] **BL-091** Make placement consume the cop action. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-092** Store exact declared barrier coordinate. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-093** Increment barrier count exactly once. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-094** Keep new barriers permanent. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-095** Make barriers impassable to both roles. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-096** Grandfather immediate cop occupancy on own-cell placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-097** Forbid cop re-entry after leaving own-cell barrier. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-098** Do not consume quota on rejected placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-099** Do not advance turn on rejected placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-100** Test barrier-set/count invariant after every transition. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Capture claims

- [ ] **BL-101** Define common Capture Claim type. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-102** Define coordinate-overlap capture cause. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-103** Define barrier-on-thief capture cause. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-104** Define trapped-thief capture cause. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-105** Require cop as Capture Claim issuer. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-106** Reject thief-issued Capture Claim. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-107** Reject claim with wrong capture cause. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-108** Reject claim when factual predicate is false. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-109** Accept claim when matching factual predicate is true. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-110** Preserve state on rejected Capture Claim. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Trapped capture

- [ ] **BL-111** Enumerate orthogonal thief destinations only. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-112** Exclude off-board destinations. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-113** Exclude barrier destinations. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-114** Exclude STAY from escape destinations. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-115** Detect no-destination trapped state. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-116** Require common local claim boundary. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-117** Evaluate trap after accepted relevant transition. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-118** Keep trap detection deterministic. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-119** Test corner and edge trapping. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-120** Test near-trap with one legal escape. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## End ordering

- [ ] **BL-121** Evaluate coordinate capture before survival. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-122** Evaluate barrier capture before survival. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-123** Evaluate trapped capture before survival. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-124** Apply capture priority on threshold step. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-125** Apply survival only without capture. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-126** Represent technical loss without detecting it. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-127** Reject mutation after capture. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-128** Reject mutation after survival. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-129** Reject mutation after technical loss. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-130** Make repeated end evaluation idempotent. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Scoring

- [ ] **BL-131** Map capture to cop 20 and thief 5. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-132** Map survival to cop 5 and thief 10. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-133** Map technical loss to 0 and 0. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-134** Keep series tie score 2 outside Stage 1. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-135** Reject scoring a nonterminal state. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-136** Reject unsupported outcome kinds. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-137** Reject capture cause on non-capture outcome. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-138** Return equal scores on repeated evaluation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-139** Test every capture cause uses capture scores. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-140** Prevent configuration from overriding fixed scores. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Adversarial tests

- [ ] **BL-141** Test every orthogonal direction from interior cells. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-142** Test every orthogonal direction at board edges. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-143** Test diagonal rejection without mutation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-144** Test off-board rejection without mutation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-145** Test barrier collision without mutation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-146** Test wrong-role action without mutation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-147** Test invalid barrier without quota consumption. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-148** Test action after terminal outcome. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-149** Test malformed initial state rejection. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-150** Test multiple complete runs for repeatability. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Traceability

- [ ] **BL-151** Link BL-AC-01 to configuration/state tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-152** Link BL-AC-02 to rejection tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-153** Link BL-AC-03 to movement tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-154** Link BL-AC-04 to atomic rejection tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-155** Link BL-AC-05 to valid barrier tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-156** Link BL-AC-06 to barrier rejection tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-157** Link BL-AC-07 to grandfathered occupancy tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-158** Link BL-AC-08 and BL-AC-09 to capture tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-159** Link BL-AC-10 and BL-AC-11 to ordering/scoring tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-160** Link BL-AC-12 to fresh-process repeatability evidence. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Verification

- [ ] **BL-161** Run the complete future Stage 1 test suite. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-162** Run the future lint gate. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-163** Run the future 150-line check. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-164** Run git diff check. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-165** Scan tracked files for secrets. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-166** Confirm no Stage 2-7 dependency was added. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-167** Perform Codex-assisted adversarial review. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-168** Correct ordinary defects found by review. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-169** Record commands exit codes and results. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-170** Merge only through an approved verified Pull Request. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Completion gate

Stage 1 completes only after every applicable task is finished, acceptance criteria have tests, evidence records exact results, adversarial defects are corrected, and a Pull Request is approved and merged.
