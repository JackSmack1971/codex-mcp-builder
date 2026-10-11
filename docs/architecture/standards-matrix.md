# Standards implementation matrix (2026-10-10)

| Standard/source | Normative vs guidance | What to check |
|---|---|---|
| https://modelcontextprotocol.io/specification/2026-07-28 | MCP normative | JSON-RPC; stateless requests; capability negotiation; server/discover; tools/resources/prompts |
| https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization | MCP normative for supported HTTP auth | Protected-resource metadata; resource indicators; token audience; issuer and scope; per-request bearer token |
| https://modelcontextprotocol.io/specification/draft/changelog | DRAFT, not automatically binding | Proposed future changes only; do not silently implement draft |
| https://ts.sdk.modelcontextprotocol.io/v2/ | SDK docs | v2 package APIs and transport adapters |
| https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28 | SDK migration docs | Explicit modern wire opt-in and 2025 fallback behavior |
| https://py.sdk.modelcontextprotocol.io/get-started/ | SDK docs | Python API and tested in-memory client patterns |
| https://developers.openai.com/plugins/build/mcp-server | Host integration guidance | Tool UX, auth, annotations, accounts and deployment requirements |
| https://developers.openai.com/codex/config-reference | Host engineering reference | Codex configuration, agents and MCP client settings |

Requirements must be classified: MUST/SHOULD/MAY from the pinned spec, host-specific, SDK implementation detail, or project recommendation. Do not equate release candidate, draft extension, and stable core requirements.
