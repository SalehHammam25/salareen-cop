# Stage 3 Blind Strategy Verification

Date: 2026-08-17

## Delivery context

- Branch: `feat/cop-stage-3-blind-strategy`, stacked directly on
  `feat/cop-stage-2-mcp-infrastructure`.
- Stage 2 base commit:
  `3fccadd9384a4510463d5b09c92e2144deacc0c4`.
- Stage 1 and Stage 2 remain unmerged while GitHub Pull Requests are unavailable.
- No Pull Request or merge was performed, and Stage 4 was not started.
- The sibling thief repository was inspected read-only as a plugin/fallback
  compatibility reference; its escape objective and opponent snapshot were not copied.

## Authority review

The requirements PDF was inspected for Chapter 6, Chapter 10.3.3, Appendix E
rules 13-16 and 25, and Annex F Tables 13, 15, and 22. Appendix E makes
orthogonal movement and truthful barrier placement mandatory. Rule 25 recommends
keeping movement authority outside the LLM; this repository adopts it as policy.
Annex F fixes the shared move set and identifies private `police_class` selection.

ADR-003 requires stable movement and barrier tie orders but does not state their
exact sequences. The implementation uses Annex F's listed `N, S, E, W` order,
excludes STAY except when the supplied target is already reached, and uses the same
order for adjacent barrier candidates. This missing ADR detail remains recorded as
an ambiguity rather than being represented as an explicit ADR mandate.

## Architecture and information boundary

- A frozen `StrategySnapshot` exposes board geometry, cop coordinate, permanent
  barriers, remaining cop quota, episode status, and an injected target only.
- It exposes no thief coordinate, transport/session state, scent, belief, language,
  provider, network, cryptographic, random, or wall-clock data.
- `BlindCopPolicy` performs bounded breadth-first pursuit and visits no more than
  N-squared cells.
- `ContainmentBarrierPolicy` is an optional deterministic boundary. It considers
  only legal adjacent cells near the supplied target and refuses candidates that
  remove every cop exit or make the target unreachable.
- `StrategyGateway` alone translates a proposal to `BaseLogicRules.apply`.
  Validation never mutates the supplied state; rejected proposals preserve it.
- Private TOML `[strategy].police_class` accepts only
  `module.path:ClassName`, a class, a no-argument constructor, and callable
  `propose(snapshot)`. Shared JSON and remote inputs cannot select it.
- Import, class, constructor, runtime, malformed-result, wrong-role, and illegal
  proposal failures produce visible typed, sanitized fallback through the built-in
  cop pursuit policy.

## Verification results

Every final command exited 0:

- `uv lock`: 88 packages resolved.
- `uv sync --frozen`: synchronized the locked environment.
- `uv run ruff check .`: all checks passed.
- `uv run pytest -q`: 291 passed with one upstream Authlib warning.
- Focused Stage 3 suite: 42 passed.
- Stage 1-2 regression suite with Stage 3 tests ignored: 249 passed.
- Fresh-process repeatability is included in the focused suite and passed.
- `uv run python scripts/check_python_line_lengths.py`: 79 Python files checked;
  maximum 150 lines.
- `git diff --check`: passed.
- Forbidden strategy-import and Base Logic reverse-import scans: no matches.
- Credential, private endpoint, and private-value scan over production strategy:
  no matches.

The largest new production file is `gateway.py` at 86 lines. The largest new
test file is `test_strategy_paths.py` at 107 lines.

## Intermediate failures and corrections

1. Poppler was unavailable for PDF inspection, and the first parser attempt failed
   because `pypdf` was absent. `pypdf 6.16.1` was installed transiently for
   read-only extraction; final `uv sync --frozen` removed it because it is not a
   project dependency.
2. The first focused run had 41 passes and one failure caused by two generated test
   plugins sharing an import-cache name. Unique module names corrected the test;
   the final focused run passed all 42 tests.
3. Ruff found one callable default in a test helper. Moving construction into the
   function corrected it; final Ruff passed.

## Adversarial review

- Snapshot field inspection proves thief truth and Stage 2 state are absent.
- Cop pursuit uses shortest-path movement and does not reuse thief escape behavior.
- BFS uses explicit tuple ordering and bounded visited maps; no set/dict iteration
  decides ties.
- Move and barrier proposals, including malicious diagonal, distant barrier,
  wrong-role, and hidden-thief-collision cases, cannot bypass Base Logic.
- Plugin exception messages and private references do not enter fallback reports.
- Barrier proposals never use randomness, exceed quota, duplicate barriers, leave
  the board, or knowingly eliminate every cop exit.
- No Base Logic reverse dependency, forbidden Stage 2/4-7 import, circular import,
  RL dependency, private configuration, or Python file over 150 lines was found.

## Remaining gate

`STR-065` remains unchecked. Stage 3 is not complete under the governance gate
until Stage 1, Stage 2, and Stage 3 can be reviewed and merged in order.
