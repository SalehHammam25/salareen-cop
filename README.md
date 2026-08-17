# salareen-cop

Cop peer for **Distributed Cops-and-Robbers over a Peer-to-Peer Network**, specification version 3.0.0.

## Current status

Documentation alignment is in progress for Stages 1-5. No application code, dependencies, runtime configuration, server, tunnel, or test suite exists yet. Stages 6-7 remain future work.

## Authority

- The requirements PDF v3.0.0 is authoritative.
- Appendix E is the mandatory-rule checklist.
- Annex F is the sole authority for numerical values and their fixed, minimum, or negotiable status.
- Examples and recommendations are non-mandatory unless an explicit mandatory rule incorporates them.
- The sibling `salareen-thief` repository is a read-only compatibility reference. Cop pursuit and barrier behavior remains role-specific.

## Planned stages

1. deterministic Base Logic;
2. symmetric FastMCP infrastructure;
3. cop pursuit and barrier strategy;
4. language, scent, and belief;
5. public tunneling;
6. security and cryptography (future);
7. reporting and visualization (future).

The sequence follows Chapter 10 and is a project workflow decision, not an additional specification mandate.

## Governance

Project owner: Areen. Independent human review is not required under the owner-approved policy. Review uses Codex-assisted adversarial review plus automated verification. Pull Requests and recorded verification remain mandatory. No implementation begins until the relevant PRD, PLAN section, TODO, and decisions are approved.

## Security

Never commit credentials, tokens, assigned tunnel domains, private peer endpoints, `credentials.json`, `token.json`, or private `config/game.toml`. Public shared configuration will be added only during implementation.

## Development status

There is currently nothing to install or run. Future implementation will use Python with `uv`, but this documentation branch intentionally adds no dependency or runtime files.
