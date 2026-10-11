# ADR-0001: MCP protocol and SDK target

Status: PROPOSED (must be validated for each server).
Date: 2026-10-10.

## Context
MCP 2026-07-28 shifts to stateless requests and server/discover; v2 TypeScript SDK supports it but must explicitly negotiate/serve that revision. Some hosts may still speak 2025-11-25.

## Recommended decision
Target 2026-07-28; choose stdio for local and Streamable HTTP for remote. Make legacy support an explicit compatibility decision after testing the actual target host. Default to no Tasks/Apps extension until requirements demand it.

## Consequences
May require a version-aware protocol adapter for older clients; no automatic production compatibility claim. Server-side per-request authorization required for protected remote use.

## Primary evidence
https://modelcontextprotocol.io/specification/2026-07-28
https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28
