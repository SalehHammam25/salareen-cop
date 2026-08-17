# Stage 1 Base Logic Verification

**Branch:** `feat/cop-stage-1-base-logic`

**Specification:** 3.0.0

**Technical gate:** PASS

**Delivery gate:** PENDING commit, push, Pull Request, review, and merge

## Authority and review

The implementation follows Chapter 3, Chapter 10 Stage 1 guidance, Appendix E rules 11-16, 21-22 and 46-48, Annex F Tables 13, 15 and 17, and ADR-001. Project owner Areen approved the decisions. No independent human reviewer participated. Review was Codex-assisted adversarial review plus automated verification.

## Architecture

- Installable `uv_build` src-layout package under `src/salareen_cop`.
- Empty runtime dependency set; pytest and Ruff are development-only.
- Frozen slotted configuration, coordinate, state, action-result, and outcome models.
- Strict JSON decoding detects malformed UTF-8, malformed JSON, and duplicate keys.
- Extraction and semantic validation return ordered typed rejection issues and never partial accepted configuration.
- Narrow modules separate movement, barriers, capture, state validation/factories, transitions, scoring, and rules.
- Test-only replay helpers remain under `tests/support`; production has no replay module.
- Base Logic imports no networking, MCP, strategy, LLM/provider, scent, belief, tunneling, cryptography, GUI/reporting, random, or wall-clock package.

## Shared and cop-specific behavior

All shared production modules match the approved thief Stage 1 modules after namespace substitution. The committed shared JSON carries complete Annex F defaults while Stage 1 extracts only its Base Logic subset. Cop-only behavior covers movement, barrier authority/quota, adjacent and own-cell placement, grandfathered departure, no re-entry, common local Capture Claims, coordinate/barrier/trapped capture, capture-before-survival, and exact scores.

## Failures and corrections

1. Initial full verification: 198 tests passed and one fresh-process test failed because the test-only replay JSON fixture was missing. The fixture was added; no production replay responsibility was introduced.
2. The first passing suite had 199 tests. Adversarial review added a direct cross-repository contract audit for the committed Annex F fixture and exact shared enumerated vocabulary, bringing the total to 201.
3. TODO BL-048 formerly implied a Stage 1 turn scheduler absent from the approved shared contract. It was corrected to action-role validation, avoiding cop/thief physics divergence.
4. Git ignore coverage was tightened for `credentials.json`, `token.json`, private TOML, and private configuration directories.

## Tool versions and exact results

| Command | Exit | Result |
|---|---:|---|
| `uv --version` | 0 | `uv 0.12.5 (210d1f678 2026-08-14 x86_64-pc-windows-msvc)` |
| `python --version` | 0 | `Python 3.12.10` |
| `uv lock` | 0 | Resolved 8 packages and created `uv.lock` |
| `uv sync --frozen` | 0 | Installed the package plus development tools |
| package import command | 0 | `salareen_cop` and `salareen_cop.base_logic` imported |
| first `uv run pytest -q` | 1 | 198 passed, 1 failed: missing test fixture |
| `uv run ruff check .` | 0 | All checks passed |
| final `uv run pytest -q` | 0 | 201 passed |
| line checker | 0 | 45 Python files checked; none above 150 lines; actual maximum 146 |
| shared-module compatibility audit | 0 | No mismatches after namespace substitution |
| forbidden-import scan | 1 | Expected no-match result |
| credential/domain/private-endpoint scan | 1 | Expected no-match result |
| generated-artifact tracked-file scan | 1 | Expected no-match result |
| `git diff --check` | 0 | No whitespace errors |

## Acceptance coverage

Tests cover package installation, dependency isolation, line checker behavior, configuration rejection categories, duplicate keys including ignored sections, Annex F values, immutability, coordinates/bounds, initial state, movement/STAY, all rejection paths, barriers/quota/own-cell semantics, all Capture Claims, trapping, capture priority, survival, technical loss, scoring, terminal/rejected identity, malformed runtime values, deterministic replay, fresh-process equality, and shared-rule compatibility without importing thief production code.

## Remaining delivery work

The implementation may be committed and pushed after cached-diff review. A focused Pull Request, review, merge, and synchronized `main` are still required. Stage 2 must not begin before that delivery gate passes.
