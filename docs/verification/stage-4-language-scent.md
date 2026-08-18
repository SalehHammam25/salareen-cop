# Stage 4 Language, Scent, and Belief Verification

Date: 2026-08-17

## Delivery context

- Branch: `feat/cop-stage-4-language-scent`, stacked directly on
  `feat/cop-stage-3-blind-strategy`.
- Stage 3 base commit:
  `c22d72a606a31045f168289b5b6bf13a93f0b080`.
- Stages 1-3 remain unmerged while GitHub Pull Requests are unavailable.
- No Pull Request or merge was performed, and Stage 5 was not started.
- The sibling thief repository was inspected read-only.
- The requested ADR filename does not exist. The repository authority used was
  `ADR-004-stage-4-shared-scent-language-belief.md`; the mismatch is retained.

## Authority and shared compatibility

The requirements PDF was reviewed for Chapters 4, 6.4-6.5, and 10.3.4,
Appendix E rules 23 and 25-27, and Annex F Tables 14, 16, 18, 21, and 22.
Annex F fixes center intensity `0.9`, decay `0.10`, and a 5x5 field.

The thief repository has no standalone Stage 4 fixture file. Its canonical
Stage 4 test vectors and shared production modules were therefore used as the
compatibility evidence. Every shared scent, belief, and language source file
matches after only namespace and line-ending normalization.

## Scent architecture

- Exact `Decimal` values are center `0.9`, Chebyshev ring one `0.6`,
  ring two `0.3`, and decay rate `0.10`.
- A turn applies Base Logic first, decays existing scent by exactly `0.90`,
  emits from the accepted updated position, combines by cell-wise maximum,
  clips to the board, and publishes an immutable observation.
- Rejected or blocked actions preserve the exact prior scent object.
- Edges never wrap, reflect, transfer strength, or renormalize.
- Observations contain only turn and grid; no source or objective coordinate.

## Cop belief and strategy boundary

- Belief is an immutable normalized exact-decimal distribution over publicly
  possible thief cells. Barriers and other impossible cells receive zero mass.
- Scent likelihood `1 + strength` is applied before qualitative language.
- Private reliability is constrained to `[0.5, 1.0]`, defaulting to `0.75`.
- Invalid, non-finite, contradictory, or zero-weight evidence preserves the
  previous valid belief with a typed reason.
- Maximum-probability targets use deterministic row-major tie-breaking.
- `BeliefStrategyAdapter` passes only the selected coordinate into the Stage 3
  restricted-target interface. Stage 3 proposes; Stage 1 validates. Belief
  never creates an action or mutates game state.

## Language and provider boundary

- Versioned free-language hints are untrusted and word-limited.
- ASCII and Unicode decimal digits, coordinate tuples/lists, row/column values,
  chess-style coordinates, and approved English number-word coordinate forms
  reject deterministically.
- Provider modes are `template`, `ollama`, `claude_api`, and
  `claude_cli`, selected only by ignored private TOML.
- The async provider interface returns text and actual request/response token
  counts only. It contains no action or state-control field.
- Cadence, timeout, caller cancellation, series budget, exhausted-budget
  fallback, prompt redaction, token accounting, and sanitized failure behavior
  have deterministic fake-provider tests. No external provider was called.

## Final verification

Every final command exited 0:

- `uv lock`: 88 packages resolved.
- `uv sync --frozen`: 86 packages checked.
- `uv run ruff check .`: all checks passed.
- `uv run pytest -q`: 378 passed with one upstream Authlib warning.
- Focused Stage 4 suite: 87 passed; 291 earlier-stage tests deselected.
- Stage 1-3 regression suite with Stage 4 tests ignored: 291 passed.
- `uv run python scripts/check_python_line_lengths.py`: 110 Python files
  checked; maximum 150 lines.
- `git diff --check`: passed.
- Shared-module namespace-normalized comparison: no mismatches.
- Credential, endpoint, future-stage, networking, reverse-dependency, and
  provider-to-action scans: no production matches.

The largest new production file is `scent/config.py` at 107 lines. The
largest new test file is `test_stage4_verbal_service.py` at 149 lines.

## Intermediate failures and corrections

1. The exact requested ADR path was absent; the actual repository ADR-004 file
   was located and used without silently renaming it.
2. The first focused command used a shell glob unsupported by this PowerShell
   invocation and collected no tests. The corrected pytest name filter ran.
3. The first collected Stage 4 run had 77 passes and four failures. Three were
   caused by Unicode digit corruption during read-only source transfer; explicit
   Unicode escapes restored the intended adversarial values.
4. The fourth failure assumed every finite Decimal uniform-prior cell was
   bit-identical despite the exact normalization residual. Repeatability and a
   separate exact two-cell maximum tie are now tested independently.

## Adversarial review

- No cop component receives the thief's objective coordinate.
- Decimal arithmetic, transition order, maximum overlap, clipping, and decay
  match the thief implementation exactly.
- Unicode digits and approved number-word coordinate forms cannot bypass hint
  validation; prohibited context is removed before provider calls.
- Belief updates remain normalized and invalid evidence preserves object identity.
- Provider results expose neither actions nor state and cannot call the strategy
  or Base Logic boundary.
- Prompts, credentials, exception messages, and private provider values do not
  appear in public fallback results.
- Base Logic has no strategy or Stage 4 reverse dependency; strategy imports no
  language/provider implementation; Stage 4 imports no Stage 5-7 package.

## Remaining gate

`LSB-065` remains unchecked. Stage 4 is not complete under the governance gate
until Stages 1 through 4 can be reviewed and merged in order.
