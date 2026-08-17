# TODO-02: Basic MCP Infrastructure

**Status:** Execution-ready documentation; implementation not started
**Related PRD:** `../prd/PRD-02-basic-mcp-infrastructure.md`
**Related PLAN:** `../PLAN.md`

Each item is meaningful implementation or verification work. IDs are stable and unique. Authority ownership is defined in PRD-02.

## Governance

- [ ] **MCP-001** Approve PRD-02 and ADR-002. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-002** Map Appendix E rules 1-9. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-003** Verify Annex F Table 19 transcription. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-004** Record Stage 2 non-goals. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-005** Create future Stage 2 branch. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Contract fixture

- [ ] **MCP-006** Copy the canonical shared fixture exactly. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-007** Assert protocol version 1.0-provisional. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-008** Assert exact six wire keys. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-009** Reject extra session or phase fields. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-010** Test fixture equality across repositories. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Envelope validation

- [ ] **MCP-011** Validate strict object shape. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-012** Validate correlation identifier syntax. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-013** Validate sender role values. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-014** Validate integer coordinates and nonnegative step. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-015** Return deterministic missing unknown and type errors. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Results

- [ ] **MCP-016** Define accepted result vocabulary. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-017** Define rejected result vocabulary. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-018** Preserve stable error codes. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-019** Avoid exception-message leakage. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-020** Test deterministic result serialization. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## FastMCP server

- [ ] **MCP-021** Build cop FastMCP server boundary. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-022** Expose receive_geometry exactly. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-023** Expose relay_geometry exactly. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-024** Use Streamable HTTP endpoint. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-025** Keep server state process-local. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## FastMCP client

- [ ] **MCP-026** Build opponent client connector. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-027** Call receive_geometry through relay. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-028** Validate structured responses. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-029** Return typed transport failure. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-030** Close client resources deterministically. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Orchestrator

- [ ] **MCP-031** Make orchestrator sole transport gateway. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-032** Keep Base Logic outside transport state. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-033** Store explicit local session identity. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-034** Enforce legal phase transitions. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-035** Reject messages in terminal phase. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Duplicate policy

- [ ] **MCP-036** Cache identical validated request result. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-037** Reject correlation content mismatch. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-038** Bound FIFO history to 100. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-039** Keep history local to one process. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-040** Test deterministic eviction and fresh sessions. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Reliability

- [ ] **MCP-041** Load agreed response timeout. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-042** Load agreed watchdog timeout. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-043** Load minimum backoff 5 seconds. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-044** Load minimum retries 3. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-045** Bound every wait and retry. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Isolation

- [ ] **MCP-046** Run cop and thief in separate processes. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-047** Use separate private config roots. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-048** Prohibit shared mutable memory. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-049** Prohibit runtime file shortcuts. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-050** Test process teardown and reaping. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Integration

- [ ] **MCP-051** Start two localhost peer processes. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-052** Prove cop serves and calls. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-053** Prove thief serves and calls. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-054** Exercise both exact tools. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-055** Verify repeatable fresh-process exchange. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Adversarial

- [ ] **MCP-056** Reject malformed payload without mutation. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-057** Reject unsupported version without mutation. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-058** Reject out-of-phase message without mutation. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-059** Handle lost response with idempotent retry. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-060** Keep remote-blame attribution unresolved. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Delivery

- [ ] **MCP-061** Run focused and complete tests. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-062** Run lint and line-length gates. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-063** Scan for secrets and shared-state imports. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-064** Record verification evidence. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]
- [ ] **MCP-065** Merge only through verified Pull Request. [Authority: PRD-02; PLAN Stage 2; Appendix E and Annex F via the PRD authority matrix]

## Completion gate

Stage 2 completes only after every applicable task is finished, acceptance criteria have tests, evidence records exact results, adversarial defects are corrected, and a Pull Request is approved and merged.
