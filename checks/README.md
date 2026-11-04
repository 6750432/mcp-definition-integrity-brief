# Runnable checks

Self-contained Python 3.10+ scripts. No third-party Python packages.

## 1. `minimal_repro.py` — 10 checks

Requires Node and the `server-everything` package:

```bash
NODE=/path/to/node \
SERVER=/path/to/node_modules/@modelcontextprotocol/server-everything/dist/index.js \
python3 minimal_repro.py
```

Expected:

```text
10/10 checks passed
```

It covers:

- full JCS digest vs four-field digest (`execution`, `title`, `outputSchema`, `instructions`)
- same-scope fork visibility
- `list_changed` with unchanged definitions
- 24 fixed tool-order permutations
- order rotation warning

## 2. `drift_http_fixture.py` + `mcp_order_probe.py`

Start the fixture in one terminal:

```bash
python3 drift_http_fixture.py
# listening on 127.0.0.1:3020
```

Probe it:

```bash
python3 mcp_order_probe.py --url http://127.0.0.1:3020/mcp --probes 3
```

Expected:

```text
order:      INFO — fewer than two tools; order is not observable
definition: CHANGED
```

The fixture returns `execution: null` on the first `tools/list`, then
`{"taskSupport": "required"}`. The full-object digest changes; the four-field
digest does not.

`mcp_order_probe.py` also accepts `--json` and `--strict`, and falls back to
legacy `initialize` if `server/discover` is not implemented.

## 3. Modules

- `jcs.py` — RFC 8785 canonicalization.
- `definition.py` — `mcp-tool-definition/v1` digest and order helpers.

## Boundary

Local fixtures only. This is not a vulnerability scanner and makes no claim
about any production server.
