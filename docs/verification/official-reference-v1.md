# Official reference-v1 interoperability evidence

Date: 2026-08-19

Salareen's official adapter was checked against amireman's exact pinned Police
implementation at commit `0e976b06b1920fd5ed161ad1909d980bfa9962a4`.

- The closed agreement contains exactly 14 terms and uses `setting="Haifa"`.
- The terms SHA-256 is
  `ad9e1bfd724e9debcde523833381cb7982a5d619d693d3738b59e0da61f4d81a`.
- The published commit-reveal vector is
  `4047830b8108320cbf48c1c1e1f09c6c0d47da51c225ce2cf40c7857cefc3030`.
- The unified FastMCP server exposes only the required opponent-facing tools:
  `negotiate(message)`, `receive_turn(message)`, `submit_audit(payload)`, and
  `receive_control(message)`.
- A six-game in-process cross-implementation run passed role alternation, mutual
  per-game audits, result agreement, and final consensus.
- A six-game localhost HTTP `/mcp` run against the pinned implementation also
  passed. It completed in 222.67 seconds and both sides derived consensus SHA
  `cbd54105eee6ab3f949ae41432d4dcbb7300c8f8e5979ebdc2494d7778927ee4`.
- Cop full suite: 477 passed. Ruff and the 150-line source gate passed.
- Thief full suite: 470 passed. Ruff and the 150-line source gate passed.

The public stable domain is an operator-managed deployment value and is not stored
in Git. A live tunnel check remains required immediately before the friendly.
