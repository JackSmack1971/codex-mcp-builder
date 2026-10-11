# MCP server contract (template)

Status: NOT APPROVED. Server identity: TBD. Protocol: target 2026-07-28. Optional legacy support: undecided.

## Tool inventory
| Canonical name | User goal | Read/write risk | Input/output schema | Auth scopes / resource checks | Side effects | Idempotency | Limits |
|---|---|---|---|---|---|---|---|
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Resources and prompts
State whether needed; identify URIs, MIME types, data classification and trust boundary. Never treat resource content as instructions.

## Contract properties
Tool list deterministic; naming/version changes reviewed; inputs bounded; output typed when useful; errors safe; annotations accurately reflect observed behavior. Authorization always server-side.

## Transport/revision profile
Modern `server/discover`, statelessness and routing headers; optional 2025-11-25 legacy tests. Modern SDK choice does not imply modern wire protocol is active.
