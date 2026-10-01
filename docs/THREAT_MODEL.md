# Threat Model

## Assets

- source code integrity
- CI workflow integrity
- runtime secrets
- application availability
- container image integrity
- dependency supply chain

## Trust boundaries

1. developer workstation -> GitHub
2. repository -> GitHub Actions runner
3. CI runner -> package registries/actions
4. container -> application process
5. application -> PostgreSQL

## Threats and controls

| Threat | Control |
|---|---|
| Secret disclosure | `.env` ignored; runtime secret required |
| Vulnerable dependency | pip-audit + Dependabot |
| Vulnerable image | Trivy + Docker updates |
| Unsafe Python pattern | Bandit |
| Excessive CI permissions | `contents: read` |
| Privilege escalation | non-root + no-new-privileges + read-only FS |
| Clickjacking | X-Frame-Options + CSP |
| Host header abuse | ALLOWED_HOSTS |
| Debug exposure | debug off by default |

## Next improvements

- immutable SHA pinning for third-party actions
- SBOM and provenance
- Kubernetes security contexts
- IaC scanning
- structured logs and monitoring
