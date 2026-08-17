# TODO-05: Cloud Exposure and Tunneling

**Status:** Execution-ready documentation; implementation not started
**Related PRD:** `../prd/PRD-05-cloud-exposure-and-tunneling.md`
**Related PLAN:** `../PLAN.md`

Each item is meaningful implementation or verification work. IDs are stable and unique. Authority ownership is defined in PRD-05.

## Governance

- [ ] **CLD-001** Approve PRD-05 and ADR-005. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-002** Map Appendix E rules 1-2 6-7 and 10. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-003** Verify Annex F Table 19. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-004** Record two-machine blocker. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-005** Create future Stage 5 branch. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Provider boundary

- [ ] **CLD-006** Define provider-neutral tunnel interface. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-007** Define typed ready result. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-008** Define typed failure result. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-009** Keep provider outside gameplay logic. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-010** Test provider fake deterministically. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Private config

- [ ] **CLD-011** Load assigned domain privately. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-012** Load opponent endpoint privately. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-013** Never read token into application config. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-014** Reject absent required remote values. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-015** Hide private values from repr. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Endpoint validation

- [ ] **CLD-016** Require public HTTPS. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-017** Reject localhost and private IP. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-018** Reject userinfo and fragments. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-019** Reject malformed ports. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-020** Normalize only safe components. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Redaction

- [ ] **CLD-021** Redact secret query keys. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-022** Redact private endpoint diagnostics. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-023** Avoid raw exception leakage. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-024** Avoid token process arguments. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-025** Test safe display output. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Lifecycle

- [ ] **CLD-026** Wait for local MCP readiness. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-027** Start tunnel with bounded deadline. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-028** Verify assigned public endpoint. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-029** Probe health without secrets. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-030** Stop idempotently and reap process. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Failures

- [ ] **CLD-031** Type DNS failure. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-032** Type TLS failure. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-033** Type disconnect and timeout. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-034** Type provider and process exit. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-035** Keep ambiguous attribution unknown. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Retry

- [ ] **CLD-036** Use shared minimum backoff 5 seconds. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-037** Use shared minimum retries 3. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-038** Propagate cancellation. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-039** Return one exhaustion result. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-040** Prevent unbounded reconnect loops. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Watchdog

- [ ] **CLD-041** Use negotiated watchdog default 60 seconds. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-042** Pause gameplay on disconnect. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-043** Evaluate local path health. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-044** Avoid premature blame. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-045** Surface watchdog state. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Resume identity

- [ ] **CLD-046** Compare exact game ID. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-047** Compare exact session ID. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-048** Compare exact protocol version. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-049** Compare exact turn index and phase. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-050** Abort mismatch without winner. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Stable domain

- [ ] **CLD-051** Reuse same assigned domain. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-052** Reject unexpected provider URL. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-053** Keep domain out of Git. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-054** Verify restart endpoint stability. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-055** Document operator-only evidence. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Remote acceptance

- [ ] **CLD-056** Expose cop endpoint on machine one. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-057** Reach thief endpoint on machine two. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-058** Prove symmetric public calls. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-059** Complete one remote match. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-060** Record blocker until evidence exists. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Delivery

- [ ] **CLD-061** Run fake-provider and local tests. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-062** Run redaction and secret scans. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-063** Run authorized public verification later. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-064** Record verification evidence. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]
- [ ] **CLD-065** Merge only through verified Pull Request. [Authority: PRD-05; PLAN Stage 5; Appendix E and Annex F via the PRD authority matrix]

## Completion gate

Stage 5 completes only after every applicable task is finished, acceptance criteria have tests, evidence records exact results, adversarial defects are corrected, and a Pull Request is approved and merged.
