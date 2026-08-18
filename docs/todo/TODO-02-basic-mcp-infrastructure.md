# TODO-02: Basic MCP Infrastructure

**Status:** Implementation complete on stacked branch; Pull Request and merge pending
**Related PRD:** `../prd/PRD-02-basic-mcp-infrastructure.md`
**Related PLAN:** `../PLAN.md`

Each item is meaningful implementation or verification work. IDs are stable and unique. Authority ownership is defined in PRD-02.

## Governance

- [x] **MCP-001** Approve PRD-02 and ADR-002. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-002** Map Appendix E rules 1-9. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-003** Verify Annex F Table 19 transcription. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-004** Record Stage 2 non-goals. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-005** Create future Stage 2 branch. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Contract fixture

- [x] **MCP-006** Copy the canonical shared fixture exactly. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-007** Assert protocol version 1.0-provisional. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-008** Assert exact six wire keys. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-009** Reject extra session or phase fields. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-010** Test fixture equality across repositories. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Envelope validation

- [x] **MCP-011** Validate strict object shape. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-012** Validate correlation identifier syntax. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-013** Validate sender role values. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-014** Validate integer coordinates and nonnegative step. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-015** Return deterministic missing unknown and type errors. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Results

- [x] **MCP-016** Define accepted result vocabulary. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-017** Define rejected result vocabulary. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-018** Preserve stable error codes. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-019** Avoid exception-message leakage. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-020** Test deterministic result serialization. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## FastMCP server

- [x] **MCP-021** Build cop FastMCP server boundary. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-022** Expose receive_geometry exactly. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-023** Expose relay_geometry exactly. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-024** Use Streamable HTTP endpoint. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-025** Keep server state process-local. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## FastMCP client

- [x] **MCP-026** Build opponent client connector. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-027** Call receive_geometry through relay. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-028** Validate structured responses. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-029** Return typed transport failure. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-030** Close client resources deterministically. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Orchestrator

- [x] **MCP-031** Make orchestrator sole transport gateway. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-032** Keep Base Logic outside transport state. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-033** Store explicit local session identity. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-034** Enforce legal phase transitions. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-035** Reject messages in terminal phase. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Duplicate policy

- [x] **MCP-036** Cache identical validated request result. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-037** Reject correlation content mismatch. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-038** Bound FIFO history to 100. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-039** Keep history local to one process. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-040** Test deterministic eviction and fresh sessions. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Reliability

- [x] **MCP-041** Load agreed response timeout. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-042** Load agreed watchdog timeout. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-043** Load minimum backoff 5 seconds. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-044** Load minimum retries 3. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-045** Bound every wait and retry. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Isolation

- [x] **MCP-046** Run cop and thief in separate processes. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-047** Use separate private config roots. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-048** Prohibit shared mutable memory. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-049** Prohibit runtime file shortcuts. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-050** Test process teardown and reaping. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Integration

- [x] **MCP-051** Start two localhost peer processes. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-052** Prove cop serves and calls. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-053** Prove thief serves and calls. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-054** Exercise both exact tools. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-055** Verify repeatable fresh-process exchange. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Adversarial

- [x] **MCP-056** Reject malformed payload without mutation. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-057** Reject unsupported version without mutation. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-058** Reject out-of-phase message without mutation. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-059** Handle lost response with idempotent retry. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-060** Keep remote-blame attribution unresolved. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Delivery

- [x] **MCP-061** Run focused and complete tests. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-062** Run lint and line-length gates. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-063** Scan for secrets and shared-state imports. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [x] **MCP-064** Record verification evidence. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-065** Merge only through verified Pull Request. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Completion gate

Stage 2 completes only after every applicable task is finished, acceptance criteria have tests, evidence records exact results, adversarial defects are corrected, and a Pull Request is approved and merged.

## Live-match composition backlog

- [ ] **LM-MCP-001** Implement strict schemas and tools from live-match-orchestration-v1 without changing the six-field geometry envelope.
- [ ] **LM-MCP-002** Enforce configured expected-opponent role and test `WRONG_EXPECTED_ROLE` without claiming authentication.
- [ ] **LM-MCP-003** Implement validation order, shared rejection vocabulary and mutating-message idempotency keys.
- [ ] **LM-MCP-004** Add byte-identical initialization, normal-turn, barrier, duplicate-ack and terminal fixtures.
- [ ] **LM-MCP-005** Test lost acknowledgement, duplicate mismatch, FIFO retention and fresh-process replay.
