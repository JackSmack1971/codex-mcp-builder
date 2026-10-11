# MCP Server Engineering Control Plane (Codex CLI)

Reusable repository starter for building MCP servers under Codex CLI. Research cutoff: 2026-10-10. The 2026-07-28 MCP spec is the target; backward compatibility is an explicit product decision, not an assumption.

## What this package is

It is **instructions, reusable Skills, specialized agent definitions, validation checks, and design templates**. It is not an MCP server, an authorization system, or a substitute for runtime enforcement. It makes no production-readiness claim.

## Quick start

1. Extract into the root of a **new** project or carefully merge into an existing repository; review existing `AGENTS.md`, `.codex/`, `.agents/` first. Do not overwrite existing configuration.
2. Open the repository in Codex CLI. Review effective sandbox, approvals, allowed networking and installed toolchain independently. Do not treat the repo config as an access grant.
3. Invoke `$mcp-discovery` for a new server or audit, then `$mcp-contract-design`; require acceptance of `docs/contracts/server-contract.md` before implementation.
4. Invoke `$mcp-implementation` to implement one slice at a time, then `$mcp-security-review` and `$mcp-conformance` using independent review.
5. Invoke `$mcp-release` only after the conformance and security gates have evidence. Deploy/publish only under separate explicit authorization.
6. Run `python scripts/validate_control_plane.py` to check package structure and internal references (not MCP server behavior).

## Defaults and decisions

- Protocol target: MCP **2026-07-28**; negotiate modern explicitly and test any desired 2025-11-25 compatibility.
- Default transport: stdio for local subprocess integrations; Streamable HTTP for remotely hosted services. Legacy SSE is not a new-server default.
- Default SDK: TypeScript v2 for TypeScript stacks (`@modelcontextprotocol/server`); Python's current SDK for Python stacks. Pin tested versions in the target project's package manifest after validation.
- Modern MCP is stateless at the protocol layer. Don't assume a session ID, sticky sessions, or per-connection dynamic tool catalog. For durable workflows use caller-bound handles and opt-in Tasks if the client supports it.
- Choose minimum capability surface. Tools are operations; Resources are context/data; Prompts are reusable interaction templates. Extensions only when supported and needed.
- Authorization: per-request identity, resource/audience and scope checks for protected remote endpoints; tool-level authorization including argument/resource ownership; upstream credentials never forwarded indiscriminately.
- No live external writes, account changes, publication, trade execution, or deployment without separately authorized action.

## Layout

`AGENTS.md`: persistent engineering behavior. `.codex/config.toml`: non-authoritative orchestration defaults. `.codex/agents/`: role specialists. `.agents/skills/`: on-demand engineering runbooks. `docs/`: decisions and evidence templates. `scripts/validate_control_plane.py`: package integrity and structural checks.

## Current references (verified 2026-10-10)

- https://modelcontextprotocol.io/specification/2026-07-28
- https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization
- https://modelcontextprotocol.io/specification/2026-07-28/changelog
- https://ts.sdk.modelcontextprotocol.io/v2/
- https://ts.sdk.modelcontextprotocol.io/v2/migration/support-2026-07-28
- https://py.sdk.modelcontextprotocol.io/get-started/
- https://developers.openai.com/plugins/build/mcp-server
- https://developers.openai.com/codex/guides/agents-md
- https://developers.openai.com/codex/config-reference

When sources disagree, record the precise conflict, target client/SDK versions, and executed compatibility evidence. OpenAI integration guidance may lag current MCP SDK package layout; check SDK release-specific docs rather than assuming a single package applies to all versions.

## Supreme-derived control-plane audit extension

The supplied CP-001 through CP-058 requests were reviewed sequentially. See `docs/verification/cp-001-058-dispositions.md` for the per-prompt disposition and `docs/governance/operating-procedures.md` for the consolidated safe workflows. `docs/governance/decisions.md` records open authorization and host-dependent questions. This is **not** a claim that all prompts are enforceable or fully implemented.

For read-only change-surface verification, capture a baseline with `python scripts/audit_repository.py --output baseline.json` from a **separate** evidence directory, and later run `python scripts/audit_repository.py --baseline baseline.json --expected allowed-paths.json`. The latter JSON must be an explicit list of allowed relative paths. Exit code 2 indicates an unexpected changed path. Do not put baseline evidence inside the target tree unless you intend to include it in the inventory. Run `python -m unittest discover -s tests -v` for its isolated unit tests.
