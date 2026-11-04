# #security-ig post (draft)

**Status:** not posted. Discord is unreachable from the author's network, and the GitHub token used for this repository is read-only on `modelcontextprotocol/modelcontextprotocol` (`CreateDiscussion` is forbidden).

**Target:** MCP Contributors Discord → `#security-ig`
**Agenda item:** Runtime drift: `list_changed` semantics after approval (Open, no champion)

---

Hi #security-ig — I'd like to pick up the open agenda item "Runtime drift: `list_changed` semantics after approval", with measurements first rather than a new proposal.

We ran a local matrix over the 7 official reference servers (1.x and 2.x, stdio; no public endpoints). Four observations:

1. 7/7 now speak 2026-07-28, but the era is connection-sticky: legacy-first makes `server/discover` return `-32601`; modern-first makes `initialize` return `-32022`.
2. 2.x adds `execution` (`taskSupport`) to some tool definitions. A four-field digest (`name` / `description` / `inputSchema` / `annotations`) does not see it; a full-object JCS digest does.
3. `notifications/tools/list_changed` can fire while the tool set and digests are unchanged. It is a re-fetch hint, not evidence.
4. Against the conformance fixtures, our checks and conformance agree on the overlapping properties (clean baseline + order, 2/2) but cover different properties; conformance passes a fixture whose `execution` changes after first approval.

Question: should the runtime-drift item recommend a full-definition pin (complete `Tool` object + server `instructions` + `serverInfo`, RFC 8785 JCS) keyed by `(authorization scope, protocolVersion)`, and treat `list_changed` as a hint rather than evidence?

Earlier fixture/PoC: https://gist.github.com/6750432/43837d3355de826dfb83f04acbda9139

I can share a sanitized package and the 2×2 matrix (`https://github.com/6750432/mcp-definition-integrity-brief`), not a 100KB attachment. No vulnerability claim; local fixtures only. I'm not asking to reopen #3452.

---
