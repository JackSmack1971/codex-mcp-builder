# MCP threat model (template)

Status: UNREVIEWED. Assets: credentials, user data, external write authority, upstream quota, tenant boundaries, service integrity.

## Trust boundaries
- Model-generated calls and fetched context are untrusted inputs.
- MCP client/tool hints cannot grant permission.
- Protected HTTP requests require per-request token validation, resource/audience and scope/object-level checks.
- Upstream services have separate credentials, rate limits and scopes.

## Threat register
| Scenario | Boundary | Preventive control | Negative test | Residual risk |
|---|---|---|---|---|
| Missing/wrong audience token | HTTP auth | deny before handler | 401 test | TBD |
| Other tenant resource ID | Object auth | owner/scope check | 403 test | TBD |
| SSRF via URL argument | Upstream egress | fixed hosts and DNS/IP controls | test | TBD |
| Prompt injection in resource | Model/data | data classification and escaping | test | TBD |
| Tool argument causes external write | Backend | scoped authorization, approvals where needed, idempotency | test | TBD |
| Token in logs or errors | Telemetry | redaction | test | TBD |

## Security review
Name reviewer, baseline commit, findings, resolved controls, remaining risks and test evidence.
