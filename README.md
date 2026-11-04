# MCP definition integrity — sanitized brief

Local measurements and test vectors for MCP 2.x tool-definition integrity, dual-era behavior, and order stability. Collected on 2026-11-04 from the 7 official reference servers and local fixtures.

**This is not a vulnerability scan and not a claim about any production server.** No public endpoints, credentials, hostnames, private paths, or account identifiers are included.

## Files

- `MCP-checkup-2026-11-04-v2.md` — main package: findings, minimal reproduction, full test code, 2×2 cross-check against the official conformance fixtures.
- `mcp-checkup-2026-11-04.json` — reproducible baseline (versions, tool counts, JCS digests).
- `tool-pinning-server-context.diff` — proposed additions to the public *Client-Held Tool Definition Pinning* draft: server-level `instructions`, `execution`, era/scope key, and test vectors.

## Scope

```text
7 official reference servers (1.x / 2.x), local stdio
local authenticated HTTP fixture, local drift fixture
no public network, no credentials, no production servers
```

## License

No license declared yet. Contact the author before redistributing.
