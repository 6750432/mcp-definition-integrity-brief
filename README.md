# MCP definition integrity — sanitized brief

Local measurements and test vectors for MCP 2.x tool-definition integrity, dual-era behavior, and order stability. Collected on 2026-11-04 from the 7 official reference servers and local fixtures.

**This is not a vulnerability scan and not a claim about any production server.** No public endpoints, credentials, hostnames, private paths, or account identifiers are included.

## Files

- `MCP-checkup-2026-11-04-v2.md` — main package: findings, minimal reproduction, full test code, 2×2 cross-check against the official conformance fixtures.
- `mcp-checkup-2026-11-04.json` — reproducible baseline (versions, tool counts, JCS digests).
- `tool-pinning-server-context.diff` — proposed additions to the public *Client-Held Tool Definition Pinning* draft: server-level `instructions`, `execution`, era/scope key, and test vectors.
- `checks/` — runnable Python checks: minimal 10-check repro, HTTP order probe, drift fixture. See [`checks/README.md`](checks/README.md).

## Runnable checks

```bash
# 10 checks: digest blind spots, scope fork, list_changed, 24 order permutations
NODE=/path/to/node \
SERVER=/path/to/server-everything/dist/index.js \
python3 checks/minimal_repro.py

# definition drift + order probe against a local fixture
python3 checks/drift_http_fixture.py &
python3 checks/mcp_order_probe.py --url http://127.0.0.1:3020/mcp --probes 3
```

Expected: `10/10 checks passed`; the drift fixture reports `definition: CHANGED`
and `order: INFO` (one tool, so order is not observable).

## What it measures

```text
definition  complete Tool object + instructions + serverInfo, RFC 8785 JCS, SHA-256
order       wire order of tool names across repeated tools/list calls
era         legacy initialize vs 2026-07-28 server/discover, connection-sticky
scope       same tool name under different auth scopes
```

## Scope

```text
7 official reference servers (1.x / 2.x), local stdio
local authenticated HTTP fixture, local drift fixture
no public network, no credentials, no production servers
```

## License

No license declared yet. Contact the author before redistributing.
