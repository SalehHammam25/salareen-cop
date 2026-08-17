# Local live-match runner

From this repository, start the cop peer with a private journal:

```powershell
$env:SALAREEN_COP_JOURNAL='.runtime/cop-match.sqlite3'
$env:SALAREEN_COP_EVENT_LOG='.runtime/cop-match.jsonl'
uv run python -m salareen_cop.live_match.runner --host 127.0.0.1 --port 8802 `
  --opponent http://127.0.0.1:8801/mcp --game-id local-game `
  --session-id local-session --scenario capture
```

The peer exposes `/mcp`. Local mode uses loopback HTTP only. Remote mode requires
the exact configured public HTTPS host, permitted port and `/mcp` path. Never put
credentials in an endpoint, journal, command line or log.

Start the thief independently on port 8801, then run
`uv run python tests/support/live_match_process_probe.py`. Stop both peer
processes after the probe. This runbook does not start ngrok.
