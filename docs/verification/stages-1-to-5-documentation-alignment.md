# Stages 1-5 Documentation Alignment Verification

**Branch:** `docs/cop-stages-1-to-5-alignment`

**Scope:** Documentation and README only; no implementation, dependency, runtime configuration, service, tunnel, or Pull Request.

## Review policy

Project owner: Areen. Independent human reviewer: none required under the owner-approved policy. Review method: Codex-assisted adversarial review plus automated verification. Pull Requests and verification remain mandatory for delivery.

## Appendix E ownership

| Rules | Stage owner | Documentation |
|---|---:|---|
| 1-2 | 2 and 5 | process separation and no shared state |
| 3-9 | 2 | orchestrator, state machine, bounded waits, watchdog, local truth |
| 10 | 5 | public tunnel |
| 11-16 | 1 | shared configuration, movement, and barrier truth |
| 17-20 | 6 future | Commit-Reveal, audit, replay |
| 21-22 | 1 boundary; 6 proof | truthful Capture Claim and later cryptographic enforcement |
| 23 | 4 deterministic model; 6 lock | scent model becomes lockable in Stage 4 |
| 24 | 6 future | Step-0 hardware declaration |
| 25-27 | 3-4 | deterministic actions, natural language, no numeric location protocol |
| 28-45 | 7 future | reporting, Gmail, league, repositories, submission |
| 46-48 | 1 | barrier/trapped capture and fixed score pairs |
| 49-55 | 6-7 future | repository/reporting/league additions |

Every mandatory rule with executable ownership in Stages 1-5 therefore has a named PRD/PLAN owner. Split rules explicitly retain their later cryptographic or reporting enforcement owner.

## Annex F values used by Stages 1-5

- Board: 7x7 minimum; exactly two agents fixed; origin/index/starts negotiable.
- Actions: N/S/E/W/STAY fixed; barriers 14 minimum; move ceiling 35 minimum; survival threshold 35 minimum.
- Scent: center 0.9 fixed; decay 0.10 fixed; field 5x5 fixed.
- Scores: capture 20/5, survival 5/10, series tie 2, and technical loss 0/0 fixed.
- Language: area negotiable; hint limit default 15 negotiable.
- Network: 30 requests/minute minimum, concurrency 2 minimum, backoff 5 seconds minimum, retries 3 minimum, queue 100 minimum; response 30 seconds and watchdog 60 seconds negotiable.

The Stage 2 FIFO duplicate-history bound of 100 is an owner-approved compatibility decision, distinct from Annex F queue depth 100.

## Retained blockers

- No implementation or tests exist in the cop repository.
- Stage 5 needs a compatible cop runtime, second machine, authorized stable-domain private configuration, bidirectional public calls, and a complete remote match.
- Stage 6-7 requirements are future work.
- Series-count, counted-game, timeout-example, and simplified/full commitment tensions remain unresolved outside the current owning stages.

## Verification expectations

Before commit, verify documentation-only scope, unique task IDs and expected counts, no Stage 1-5 placeholders, no mojibake in aligned files, no secrets/private endpoints/domains, Appendix E ownership, Annex F values, and `git diff --check`.

## Pre-commit results

- Documentation-only scope: PASS; changed paths are `README.md` or under `docs/`.
- Task counts: PASS; Stage 1 = 170, Stages 2-5 = 65 each, total = 430.
- Stable task IDs: PASS; 430 IDs are unique and every task cites PRD, PLAN, Appendix E, and Annex F authority.
- Stage 1-5 placeholders: PASS; none remain.
- Encoding review: PASS for every aligned Stage 1-5 file.
- Sensitive-value scan: PASS; no credential, token value, assigned domain, or private endpoint is present.
- Appendix E ownership: PASS for all rules with Stage 1-5 executable ownership; split/later rules name their future owner.
- Annex F audit: PASS for every value used by Stages 1-5.
- `git diff --check`: PASS.
- Adversarial review: PASS after correcting Markdown trailing whitespace, explicit timeout defaults, task authority tags, and the distinction between duplicate-history 100 and queue-depth 100.
