# TODO-01: Base Logic

**Status:** Execution-ready documentation; implementation not started
**Related PRD:** `../prd/PRD-01-base-logic.md`
**Related PLAN:** `../PLAN.md`

Each item is meaningful implementation or verification work. IDs are stable and unique. Authority ownership is defined in PRD-01.

## Governance

- [x] **BL-001** Confirm PRD-01 owner approval is recorded. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-002** Review ADR-001 decisions against PRD-01. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-003** Map every PRD acceptance criterion to tasks. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-004** Map Appendix E rules 11-16 to owners. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-005** Map Appendix E rules 21-22 to owners. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-006** Map Appendix E rules 46-48 to owners. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-007** Verify Annex F Tables 13, 15, and 17 are transcribed exactly. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-008** Record Stage 1 non-goals before implementation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-009** Create the future focused implementation branch. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-010** Record the future Pull Request and verification gate. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Foundation

- [x] **BL-011** Initialize the future Python project with uv. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-012** Create separate source and test roots. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-013** Define the future package name for the cop peer. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-014** Add a repeatable 150-line Python-file check. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-015** Add deterministic test configuration. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-016** Add lint configuration without weakening rules. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-017** Protect virtual environments and caches in gitignore. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-018** Protect credentials and private configuration in gitignore. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-019** Record exact setup commands in verification evidence. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-020** Prove foundation imports in a clean environment. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Config schema

- [x] **BL-021** Define strict shared JSON top-level sections. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-022** Define board and agent schema fields. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-023** Define movement and barrier schema fields. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-024** Define scoring schema fields. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-025** Reject unknown shared configuration fields. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-026** Reject missing mandatory configuration fields. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-027** Reject Boolean values where integers are required. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-028** Reject malformed UTF-8 and duplicate JSON keys. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-029** Return ordered typed configuration issues. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-030** Keep private local settings outside shared JSON. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Config values

- [x] **BL-031** Enforce grid size minimum 7. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-032** Enforce exactly two agents. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-033** Validate negotiable coordinate origin. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-034** Validate negotiable starting index. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-035** Validate both negotiated starting positions. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-036** Enforce barrier quota minimum 14. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-037** Enforce max moves minimum 35. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-038** Enforce survival threshold minimum 35. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-039** Enforce equal max moves and survival threshold. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-040** Enforce fixed score values and reject overrides. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## State model

- [x] **BL-041** Define immutable coordinate representation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-042** Define immutable board representation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-043** Define explicit cop and thief roles. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-044** Define immutable positions aggregate. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-045** Define permanent barrier collection. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-046** Define placed-barrier count. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-047** Define valid-step count. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-048** Define action-role validation without inventing the later turn scheduler. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-049** Define terminal outcome model. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-050** Define score-pair model. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## State creation

- [x] **BL-051** Build initial state only from accepted configuration. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-052** Reject starting positions outside the board. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-053** Reject duplicate starting positions when configuration forbids overlap. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-054** Reject starting positions on barriers. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-055** Reject barriers outside the board. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-056** Reject barrier count above quota. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-057** Reject inconsistent stored barrier count. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-058** Prevent partial state on failed construction. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-059** Produce equal states from equal inputs. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-060** Test state hashing or equality deterministically. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Movement model

- [x] **BL-061** Define N movement delta. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-062** Define S movement delta. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-063** Define E movement delta. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-064** Define W movement delta. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-065** Define STAY zero delta. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-066** Reject diagonal displacement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-067** Reject multi-cell displacement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-068** Reject off-board destination. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-069** Reject barrier destination. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-070** Reject movement by the inactive role. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Movement transitions

- [x] **BL-071** Apply one legal movement atomically. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-072** Advance valid-step count once after accepted movement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-073** Advance active role once after accepted movement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-074** Keep state identity on rejected movement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-075** Preserve barrier collection during movement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-076** Preserve barrier quota during movement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-077** Reject combined movement and barrier action. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-078** Reject unknown action types. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-079** Reject all actions after terminal outcome. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-080** Test repeated movement sequence equality. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Barrier validation

- [x] **BL-081** Restrict barrier actions to the cop. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-082** Allow placement on the cop current cell. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-083** Allow placement on each orthogonally adjacent cell. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-084** Reject non-adjacent placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-085** Reject off-board placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-086** Reject duplicate barrier placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-087** Reject placement after quota exhaustion. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-088** Reject thief barrier placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-089** Reject combined placement and movement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-090** Return typed barrier rejection reasons. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Barrier transitions

- [x] **BL-091** Make placement consume the cop action. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-092** Store exact declared barrier coordinate. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-093** Increment barrier count exactly once. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-094** Keep new barriers permanent. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-095** Make barriers impassable to both roles. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-096** Grandfather immediate cop occupancy on own-cell placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-097** Forbid cop re-entry after leaving own-cell barrier. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-098** Do not consume quota on rejected placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-099** Do not advance turn on rejected placement. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-100** Test barrier-set/count invariant after every transition. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Capture claims

- [x] **BL-101** Define common Capture Claim type. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-102** Define coordinate-overlap capture cause. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-103** Define barrier-on-thief capture cause. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-104** Define trapped-thief capture cause. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-105** Require cop as Capture Claim issuer. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-106** Reject thief-issued Capture Claim. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-107** Reject claim with wrong capture cause. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-108** Reject claim when factual predicate is false. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-109** Accept claim when matching factual predicate is true. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-110** Preserve state on rejected Capture Claim. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Trapped capture

- [x] **BL-111** Enumerate orthogonal thief destinations only. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-112** Exclude off-board destinations. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-113** Exclude barrier destinations. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-114** Exclude STAY from escape destinations. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-115** Detect no-destination trapped state. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-116** Require common local claim boundary. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-117** Evaluate trap after accepted relevant transition. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-118** Keep trap detection deterministic. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-119** Test corner and edge trapping. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-120** Test near-trap with one legal escape. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## End ordering

- [x] **BL-121** Evaluate coordinate capture before survival. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-122** Evaluate barrier capture before survival. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-123** Evaluate trapped capture before survival. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-124** Apply capture priority on threshold step. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-125** Apply survival only without capture. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-126** Represent technical loss without detecting it. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-127** Reject mutation after capture. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-128** Reject mutation after survival. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-129** Reject mutation after technical loss. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-130** Make repeated end evaluation idempotent. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Scoring

- [x] **BL-131** Map capture to cop 20 and thief 5. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-132** Map survival to cop 5 and thief 10. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-133** Map technical loss to 0 and 0. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-134** Keep series tie score 2 outside Stage 1. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-135** Reject scoring a nonterminal state. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-136** Reject unsupported outcome kinds. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-137** Reject capture cause on non-capture outcome. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-138** Return equal scores on repeated evaluation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-139** Test every capture cause uses capture scores. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-140** Prevent configuration from overriding fixed scores. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Adversarial tests

- [x] **BL-141** Test every orthogonal direction from interior cells. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-142** Test every orthogonal direction at board edges. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-143** Test diagonal rejection without mutation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-144** Test off-board rejection without mutation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-145** Test barrier collision without mutation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-146** Test wrong-role action without mutation. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-147** Test invalid barrier without quota consumption. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-148** Test action after terminal outcome. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-149** Test malformed initial state rejection. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-150** Test multiple complete runs for repeatability. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Traceability

- [x] **BL-151** Link BL-AC-01 to configuration/state tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-152** Link BL-AC-02 to rejection tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-153** Link BL-AC-03 to movement tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-154** Link BL-AC-04 to atomic rejection tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-155** Link BL-AC-05 to valid barrier tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-156** Link BL-AC-06 to barrier rejection tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-157** Link BL-AC-07 to grandfathered occupancy tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-158** Link BL-AC-08 and BL-AC-09 to capture tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-159** Link BL-AC-10 and BL-AC-11 to ordering/scoring tests. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-160** Link BL-AC-12 to fresh-process repeatability evidence. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Verification

- [x] **BL-161** Run the complete future Stage 1 test suite. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-162** Run the future lint gate. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-163** Run the future 150-line check. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-164** Run git diff check. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-165** Scan tracked files for secrets. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-166** Confirm no Stage 2-7 dependency was added. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-167** Perform Codex-assisted adversarial review. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-168** Correct ordinary defects found by review. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [x] **BL-169** Record commands exit codes and results. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]
- [ ] **BL-170** Merge only through an approved verified Pull Request. [Authority: PRD-01; PLAN Stage 1; Appendix E and Annex F via the PRD authority matrix]

## Completion gate

Stage 1 completes only after every applicable task is finished, acceptance criteria have tests, evidence records exact results, adversarial defects are corrected, and a Pull Request is approved and merged.
