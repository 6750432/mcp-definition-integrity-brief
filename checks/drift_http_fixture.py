#!/usr/bin/env python3
"""Modern MCP HTTP fixture: same tool, execution field drifts after first list."""
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

CALLS = 0

class H(BaseHTTPRequestHandler):
    def log_message(self, *a):
        pass
    def do_POST(self):
        global CALLS
        n = int(self.headers.get("content-length", "0"))
        body = json.loads(self.rfile.read(n) or b"{}")
        method = body.get("method")
        rid = body.get("id")
        if method == "server/discover":
            result = {
                "resultType": "complete", "ttlMs": 0, "cacheScope": "private",
                "supportedVersions": ["2026-07-28"],
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "drift-fixture", "version": "1.0.0"},
            }
        elif method == "tools/list":
            CALLS += 1
            tool = {
                "name": "read_file",
                "title": "Read file",
                "description": "Read a file.",
                "inputSchema": {"type": "object", "properties": {"path": {"type": "string"}}},
                "annotations": {"readOnlyHint": True},
                "execution": None,
            }
            if CALLS >= 2:
                tool["execution"] = {"taskSupport": "required"}
            result = {"resultType": "complete", "ttlMs": 0,
                      "cacheScope": "private", "tools": [tool]}
        else:
            self.send_response(404); self.end_headers(); return
        out = json.dumps({"jsonrpc": "2.0", "id": rid, "result": result}).encode()
        self.send_response(200)
        self.send_header("content-type", "application/json")
        self.send_header("content-length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)

if __name__ == "__main__":
    ThreadingHTTPServer(("127.0.0.1", 3020), H).serve_forever()
