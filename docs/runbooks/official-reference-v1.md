# Official reference-v1 friendly

The official interoperability adapter leaves the existing live-match protocol and
strategies intact. One process serves both Salareen roles on port `8799`; expose that
single port at a stable public HTTPS URL whose path is `/mcp`.

Run from the workspace containing both `salareen-cop` and `salareen-thief`:

Bring up the endpoint before the opponent publishes its URL:

```powershell
uv run --project salareen-cop python -m salareen_cop.official.runner
```

After the opponent supplies its endpoint, stop only the local runner, keep the stable
tunnel allocated, and restart the runner on the same port with the series arguments:

```powershell
uv run --project salareen-cop python -m salareen_cop.official.runner `
  --opponent 'https://opponent.example/mcp' `
  --police-commit '<40 lowercase hex>' `
  --thief-commit '<40 lowercase hex>'
```

Add `--opponent-token` only if the opponent requires bearer authentication. Salareen
requires no incoming bearer token by default; `--incoming-token` enables one when both
sides arrange it privately.

Expose the unified local endpoint with the assigned stable tunnel domain:

```powershell
ngrok http 8799 --url "https://$env:SALAREEN_NGROK_DOMAIN"
```

Keep the runner and tunnel alive through the final `series_consensus` exchange. The
series result is written to `.runtime/official-series-result.json`; secrets and private
positions are not written there.

## Counted result reporting

For a counted match, add an empty, match-specific output directory and the stable public
MCP URL:

```powershell
uv run --project salareen-cop python -m salareen_cop.official.runner `
  --opponent 'https://opponent.example/mcp' `
  --police-commit '<Police 40-character HEAD>' `
  --thief-commit '<Thief 40-character HEAD>' `
  --public-mcp-url 'https://salareen.example/mcp' `
  --counted-result-dir '.runtime/counted/<match-label>'
```

This writes `result_<game_id>.json` only after all six games and final consensus. The
writer validates the full counted schema and refuses to overwrite an existing counted
artifact. The reporting fields are additive and never enter the
`official_reference_v1` consensus preimage.
