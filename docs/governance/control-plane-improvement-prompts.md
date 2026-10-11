# Supreme-derived Codex CLI Control Plane Improvement Prompts

Source: https://github.com/JackSmack1971/supreme (main; inspected October 10, 2026).

## Operating contract for every prompt

Apply each prompt independently and sequentially to the relevant Codex control-plane repository. Before editing: read applicable AGENTS.md, inspect Git status/diff, existing implementation/tests and supported Codex CLI version/configuration; preserve user changes. Treat Supreme's Claude-specific details as conceptual research, not Codex API facts. Verify current official Codex documentation and installed CLI help before relying on settings, approval modes, agent or sandbox capabilities. Implement only the smallest coherent slice when the capability is justified and missing; otherwise report already-satisfied or blocked. Do not modify secrets, production infrastructure, real-money trade boundaries or external systems. Do not commit/push/open PR without explicit request. Validate focused tests and relevant repository checks; report exact commands/results, changed files, blockers and uncertainty. Respect all existing accepted project decisions and phase gates. Every prompt is a research-and-implementation request, not a blanket authorization to change policy.

## Provenance and caution

Supreme's README identifies accepted invariants; its INDEX and BACKLOG distinguish partially verified material and unmigrated legacy reports. Prompts below extrapolate design patterns; they are not claimed as fully implemented in Supreme, nor as native Codex CLI features. Source anchors: README.md, AGENTS.md, INDEX.md, BACKLOG.md, knowledge/containment-auto-mode-network-and-change-surface-addendum/03-network-and-secrets-boundaries-and-change-surface.md, knowledge/claude-code-testing-research-protocol/02-the-expert-executor-architecture.md.


## P0 — Baseline, compatibility, and policy authority

### CP-001 — Codex capability and version census

**Prompt:** Inspect installed Codex CLI version, help output, supported config schema, active profiles, model/agent surfaces and official docs. Produce a source-linked capability matrix separating supported, experimental, unsupported and unknown functionality; make no config edits.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-002 — Control-plane baseline and preservation snapshot

**Prompt:** Inspect AGENTS.md hierarchy, Git status, all dirty/staged/untracked work, current policy, profiles, skills, MCPs and working directories. Produce a redacted baseline and safe rollback plan. Never reset, clean or overwrite user work.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-003 — Minimal universal AGENTS.md kernel

**Prompt:** Refactor only after auditing instruction precedence. Propose the smallest global guidance covering state preservation, local discovery, scope proportionality, credible verification, escalation and truthful reporting. Keep project-specific details local; compare instruction tokens before and after.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-004 — Instruction precedence and conflict tester

**Prompt:** Build a small deterministic fixture suite for global, repository and nested AGENTS.md plus active user instructions. Document expected precedence and conflicts, and validate behavior against the installed Codex release before adoption.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-005 — Configuration schema and drift validator

**Prompt:** Implement read-only validation of active Codex TOML/profiles/agent definitions against officially supported keys for the installed version. Fail on unknown security-relevant keys, flag experimental fields, and report drift without silently fixing settings.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-006 — Control-surface responsibility map

**Prompt:** Inventory which requirements belong in instructions, skills, rules, sandbox/approvals, dedicated wrapper, CI checks, OS permissions or human governance. Eliminate redundant prose-only controls when stronger mechanisms exist; do not assume Claude hooks map one-to-one.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-007 — Explicit policy decision register

**Prompt:** Track unresolved decisions with alternatives, consequence, authorization owner and effective scope. Preserve previously accepted decisions and prevent inferred model preferences from silently becoming architecture policy.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-008 — Profiles by consequence tier

**Prompt:** Audit existing Codex profiles and design least-privilege read-only research, ordinary implementation, offline privileged test and production-sensitive profiles. Verify command-line activation and policy precedence; never elevate privileges automatically.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

## P0 — Boundaries, safety, and containment

### CP-009 — Pre-write evidence sufficiency gate

**Prompt:** For nontrivial brownfield edits require a concise evidence record: Git ownership state, relevant instructions, toolchain, behavioral owner, nearby pattern, affected boundaries, generated/sensitive paths, oracle, expected scope and unresolved consequential ambiguity. Allow shorter paths for obvious tiny edits.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-010 — Task-local expected change surface

**Prompt:** Generate task-specific expected/protected path sets from inspection; compare the current diff against them before finalizing. Detect out-of-scope modifications and demand explicit re-reconnaissance rather than arbitrary file/line caps.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-011 — Pre-existing user work ownership ledger

**Prompt:** Distinguish user-owned dirty, staged and untracked files from agent-created artifacts. Build fixtures covering overlapping edits, renamed paths, partial staging and mixed-origin files; reject destructive operations against ambiguous ownership.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-012 — Destructive Git command guard

**Prompt:** Evaluate reliable guardrails against git clean, reset --hard, force checkout/restore, force push and bulk deletion. Prefer actual OS/host/approval enforcement where available; test safe targeted operations and blocked destructive examples. Do not mistake text instructions for enforcement.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-013 — High-consequence action taxonomy

**Prompt:** Classify remote publication, deployment, migrations, billing, revocation, permission changes, credential access and API breaks by consequence, reversibility and authorization. Specify when human approval is mandatory and when deny-and-continue is sufficient.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-014 — Windows/WSL/Linux isolation proof

**Prompt:** Build a platform matrix for native Windows, WSL2, Linux containers and disposable VMs. Test actual filesystem, network and credential reachability with harmless fixtures; never claim isolation merely because a configuration flag is set.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-015 — Network egress and remote mutation broker

**Prompt:** Design a trusted wrapper/proxy that distinguishes read-only fetches from remote writes and applies destination/method/operation policies. Prevent production or paid API mutations until expressly authorized; test fail-closed behavior and bypass paths.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-016 — Secret reachability and redaction audit

**Prompt:** Survey which secrets are visible to Codex processes, agents, shells and MCP subprocesses without printing values. Recommend narrower credentials, mounts and process isolation; verify logs and subprocess outputs redact secrets.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-017 — MCP least-privilege registry

**Prompt:** Inventory MCP servers, transports, tool names, identities, read/write effects, destinations and costs. Maintain an allowlist per profile, validate new tools before enabling, and distinguish read-only research from mutation permissions.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-018 — External tool and prompt injection boundary

**Prompt:** Create adversarial fixtures in repository documents, tool results and network responses attempting policy override, secret access and scope expansion. Verify that retrieved content remains data, not governing instruction.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-019 — Enforcement component health checks

**Prompt:** Test control-plane startup, interpreter paths, permissions, configuration parsing, wrappers, timeouts and error modes. For every claimed protection show an enforceable failure test and make unavailable protections visible instead of silently pretending to enforce.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-020 — Fail-closed production-sensitive handoffs

**Prompt:** Prove that agent research, paper trading, live execution, signing and treasury capabilities cannot cross into one another without independently enforced grants. Preserve existing P1 exit proofs and service-identity boundaries.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

## P1 — Reconnaissance and bounded implementation

### CP-021 — Adaptive brownfield reconnaissance skill

**Prompt:** Create a small reusable Codex skill for preserve → discover → localize → establish oracle → map scope → edit. Demonstrate concise and expanded paths on small and large tasks, with no requirement to read an entire repository.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-022 — Repository-native command discovery

**Prompt:** Identify actual build, lint, typecheck, test, generator and package-manager commands from project files and CI. Cache provenance with invalidation on config changes; never impose generic tool commands.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-023 — Existing-pattern and utility search

**Prompt:** Before abstractions or new helpers, search local code for equivalents, conventions and adapters. Record chosen reuse vs new implementation and verify expected behavior remains local to the requested slice.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-024 — API/schema/persistence blast-radius analyzer

**Prompt:** Identify interfaces touched by a change: public APIs, CLI flags, schemas, migrations, persistence, serialized events and runtime dependencies. Flag compatibility-impacting deltas for review; preserve versioned contracts unless explicitly authorized.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-025 — Generated/vendor/dependency boundary checker

**Prompt:** Detect generators, vendored directories, lockfiles and environment artifacts. Verify authoritative source-of-truth and required regeneration processes before modifying derived files; prevent accidental dependency churn.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-026 — Proportional implementation plan formatter

**Prompt:** Define a short change plan for multi-step work with requested outcome, relevant files, verification oracle, risks, expected scope and stopping condition. Avoid heavy planning ceremony for obvious edits.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-027 — Change-surface deviation reviewer

**Prompt:** Compare proposed implementation to scope map at checkpoints; flag unrelated formatting, public contract changes, security boundaries and new dependencies. Permit explicit evidence-backed scope changes; produce an actionable final diff audit.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-028 — Greenfield architecture decision filter

**Prompt:** Translate Supreme anti-decay lessons into contextual questions: module ownership, data flow, dependencies, failure paths and extension needs. Do not mandate Clean Architecture, vertical slices, CQRS or any universal topology.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-029 — Architecture dependency and cycle ratchets

**Prompt:** Where language tooling supports it, baseline actual dependency edges/cycles and block new unwanted violations without requiring immediate remediation of old debt. Validate signal against repository conventions and false positives.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-030 — Migration and compatibility rehearsal

**Prompt:** For schema or persistence changes, require separate migration rehearsal in disposable data, reverse/forward compatibility analysis, backups and approval of destructive operations; no production data touch.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

## P1 — Debugging, testing, and proof

### CP-031 — Evidence-led debugging workflow

**Prompt:** Implement observe → reproduce → localize → hypothesize → discriminate → fix → verify → regress. Require tests/logs supporting the root cause before claiming a fix; report nonreproducible outcomes explicitly.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-032 — Independent acceptance oracle selector

**Prompt:** Choose project-native independent oracles such as user-provided expected outputs, real API contracts, fixtures, reference implementations or end-to-end observations. Reject tests that merely encode current implementation assumptions.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-033 — Self-generated-test circularity detection

**Prompt:** Audit new tests for duplicated implementation logic, expected values computed by production code and excess mocks. Add targeted real-boundary checks where practicable; do not rewrite passing tests solely for style.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-034 — Selective independent verifier agent

**Prompt:** Trial a read-only verifier with isolated context containing requirements, interfaces and observed diff but not the implementing agent’s reasoning. Measure defect discovery and expense against a single-agent baseline; do not mandate delegation for simple tasks.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-035 — Property-based and metamorphic test selection

**Prompt:** Identify mathematical, round-trip, monotonicity, idempotence, conservation and security invariants appropriate to the project. Introduce property/metamorphic tests only where reliable independent oracles exist.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-036 — Mutation testing on high-risk code

**Prompt:** Pilot language-appropriate mutation testing on selected risk-critical modules. Report survivors and time cost; avoid universal mutation score thresholds or broad dependencies without observed benefit.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-037 — Characterization-first legacy refactor guard

**Prompt:** Before changing poorly understood legacy code, capture representative behavior and important edge cases as characterization tests, distinguishing observed behavior from desired behavior. Preserve unrelated behavior unless change is authorized.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-038 — Verification evidence manifest

**Prompt:** Produce machine-readable per-slice evidence showing exact commands, environment, start/exit status, important outputs, coverage of changed behavior, skipped checks and blockers. Prevent success claims for commands that never ran.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-039 — Completion claim semantics

**Prompt:** Define FIXED, TESTED, PASSING, PARTIALLY VERIFIED and BLOCKED based on recorded evidence, not agent confidence. Distinguish unit checks, integration checks, simulated runs and production observation.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-040 — Regression risk and targeted test selection

**Prompt:** Map modified code and interfaces to focused tests, then run repository-required broader checks. Require meaningful regression coverage while keeping unrelated flaky or expensive suites explicitly documented.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

## P1 — Memory, knowledge and orchestration

### CP-041 — Durable handoff and restart state

**Prompt:** Create compact non-secret handoffs containing task intent, Git refs, completed changes, verified commands, open decisions and next actions. Validate restart reconstruction without treating stale summaries as truth.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-042 — Evidence-backed project memory

**Prompt:** Separate authoritative repository state from agent summary and inferred preferences. Store source links, as-of dates and verification statuses; invalidate memory when relevant source changes.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-043 — Knowledge index and targeted retrieval

**Prompt:** Adapt Supreme’s frontmatter/index approach for project knowledge: concise summaries, related documents, staleness and provenance. Load topic-specific files rather than all documentation into every Codex turn.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-044 — Documentation drift and provenance checker

**Prompt:** Compare stable design decisions, config, docs and observed code for contradictions. Produce narrow actionable discrepancies; never auto-edit historical provenance to erase conflicting evidence.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-045 — Context and compaction continuity tests

**Prompt:** Test whether compacted/resumed sessions retain critical active constraints, user changes, authorization boundaries, task scope and verification failures. Preserve a minimal durable state with source pointers.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-046 — Adaptive subagent routing economics

**Prompt:** Determine when parallel research, isolated validation or code-owner tasks benefit from subagents. Set explicit handoff contracts, shared-file collision prevention and budget/time metrics; avoid mandatory agent teams.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-047 — Agent capability and privilege matrix

**Prompt:** For every role list readable sources, writable paths, executable tools, network destinations, credentials, approval authority and evidence output. Verify the actual runtime conforms and that names alone do not confer isolation.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-048 — Task checkpoint and recovery protocol

**Prompt:** Introduce reversible checkpoints around risky edits and long-running tasks. Record checksums or commit references without making unsolicited commits; test interrupted workflows and resume behavior.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-049 — Novice-readable escalation and decision UI

**Prompt:** Reduce approval fatigue by presenting only high-consequence decisions with action, impact, alternatives and safest default. Preserve autonomous ordinary edits, harmless reads and local tests.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

## P2 — Quality, governance, telemetry and evaluation

### CP-050 — Control-plane observability ledger

**Prompt:** Capture run IDs, active version/profile, applied policies, blocked actions, tool health, changed paths, test evidence, agent delegation and token/time cost. Redact secrets and avoid logging unnecessary private contents.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-051 — Safety fixture and attack simulation harness

**Prompt:** Build isolated benign fixtures for destructive command bypass, scope escape, policy tampering, fake test success, injection, network misuse and credential reachability. Report protections proven versus assumed.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-052 — Ablation and complexity budget

**Prompt:** Compare each added rule, skill, agent or wrapper to baseline tasks on correctness, regressions, interruptions, runtime, tokens and maintenance complexity. Revert ineffective additions only through an authorized reviewed change.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-053 — Codex release compatibility watch

**Prompt:** Maintain a version matrix for documented CLI options, agent configuration, skills, sandbox modes, approvals and platform differences. Detect behavior changes with executable smoke tests before any upgrade.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-054 — Change-quality ratchet without dogma

**Prompt:** Measure scope adherence, missing regression tests, unnecessary abstraction, dependency changes, observable failures and documentation drift. Set project-specific ratchets grounded in historical defects, not universal code metrics.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-055 — Research claim confidence and aging protocol

**Prompt:** Adopt Supreme’s verified/partial/stale/deprecated, source locator, as-of date and reverify-by metadata for claims about Codex APIs and runtime. Keep unsupported hypotheses out of enforceable configuration.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-056 — Hedge-fund lifecycle-aligned control-plane roadmap

**Prompt:** Classify proposed controls by executable investment lifecycle advancement, release-blocking risk or optional polish. Prioritize ingestion truth, ledger correctness, strategy isolation and paper-trade observability; avoid endless constitution-building.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-057 — Permission fatigue and deny-and-continue study

**Prompt:** Instrument safe denials, repeated denial loops and user escalation frequency. Prefer deterministic blocking with harmless alternatives, but do not allow an agent to repeatedly route around a denial.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.

### CP-058 — Final control-plane acceptance and gap audit

**Prompt:** Inspect all delivered slices, actual config and runtime behavior. Produce a matrix of requirements, implemented mechanisms, pass/fail tests, unsupported surfaces, deferred decisions and the smallest next executable improvement.

**Deliverables:** Evidence-backed disposition (implement / already present / blocked / research-only); minimal diff if implemented; focused verification and a precise handoff.
