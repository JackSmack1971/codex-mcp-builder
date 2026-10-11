# MCP server architecture (template)

Status: UNDECIDED — no server implementation included.

## User goals and non-goals
TBD

## Host/client compatibility
| Client | Version | 2026-07-28 | 2025-11-25 | Evidence |
|---|---|---|---|---|
| TBD | TBD | Not tested | Not tested | TBD |

## Stack and SDK
TBD; record tested SDK versions and explicit protocol mode.

## Transport and deployment
Choose stdio (local) or Streamable HTTP (remote), or prove a need for both. Record trust boundaries.

## Components and data flow
Host -> MCP client -> MCP server transport -> identity/authorization -> validated handler -> upstream adapter -> typed result.

## Stateless state, cache and concurrency
No implicit protocol session. Explicit handles and tenancy if needed; budgets and cleanup policy.

## Decision log
Use `docs/decisions/0001-protocol-target.md` as the starting record.
