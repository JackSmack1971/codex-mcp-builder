# Open decisions and governing boundaries

| ID | Decision | Alternatives | Authority | Default until resolved |
|---|---|---|---|---|
| GOV-01 | Supported installed Codex CLI release and config keys | Pin a tested release / defer version-sensitive controls | Repository operator | No unsupported TOML changes |
| GOV-02 | Require OS-enforced outbound mutation control | Trusted egress broker / isolated offline runtime | Security owner and operator | Do not describe prompts as egress enforcement |
| GOV-03 | Grant access to live MCP servers, credentials or paid APIs | Per-tool scoped grant / no access | Operator and service owner | No access; offline-only checks |
| GOV-04 | Cross-platform claims (Windows native, WSL2, container) | Independently test each / mark unverified | Operator | Unverified outside tested environment |
| GOV-05 | Modify published tool names, schema, MCP revision or persistence | Versioned migration / defer | Contract owner | Defer, preserve existing contract |
| GOV-06 | Activate automated Git command or filesystem guards | Host/OS-enforced gate / advisory checks only | Operator | Advisory checks; deny high-impact commands |
| GOV-07 | Permit live execution, signing or custody | Separate privilege boundary and explicit approved gate / never | Financial control owner | Never; out of scope of MCP starter |

Previously accepted project decisions must be verified in their own source repository; they are not imported into this standalone starter by inference.
