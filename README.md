# DevSecOps Pipeline

A security-focused reference project demonstrating application delivery, CI/CD, container security, dependency auditing, and secure-by-default configuration around a small Django service.

> Portfolio / learning project. The goal is to make engineering and security decisions visible, reproducible, and easy to review.

## What this project demonstrates

- Django application with a minimal health endpoint
- Secure-by-default Django settings
- Docker image running as a non-root user
- Local PostgreSQL environment with Docker Compose
- CI checks for tests, linting, SAST, dependency vulnerabilities, and container vulnerabilities
- Least-privilege GitHub Actions permissions
- Dependency update automation
- Architecture and threat-model documentation

## Pipeline

```text
Commit / Pull Request
        |
        v
+--------------------+
|   Quality Gates    |
|--------------------|
| Ruff               |
| Django checks      |
| Pytest             |
+---------+----------+
          |
          v
+--------------------+
|  Security Gates    |
|--------------------|
| Bandit (SAST)      |
| pip-audit (SCA)    |
| Trivy (container)  |
+---------+----------+
          |
          v
+--------------------+
| Container Build    |
| non-root runtime   |
+--------------------+
```

## Stack

| Area | Technology |
|---|---|
| Application | Python 3.13, Django 5.2 LTS |
| Database | PostgreSQL |
| Runtime | Gunicorn |
| Containers | Docker, Docker Compose |
| CI/CD | GitHub Actions |
| SAST | Bandit |
| Dependency audit | pip-audit |
| Container scanning | Trivy |
| Linting | Ruff |
| Tests | Pytest + pytest-django |

## Quick start

```bash
cp .env.example .env
docker compose up --build
```

Then open `http://localhost:8000/health/`.

Expected response:

```json
{"status": "ok", "service": "devsecops-pipeline"}
```

## Security controls

- secrets are injected through environment variables
- debug mode is disabled by default
- explicit allowed-host configuration
- secure cookie settings outside debug mode
- clickjacking and content-type sniffing protection
- restrictive Content Security Policy header
- Docker process runs as an unprivileged user
- Compose runtime is read-only with a temporary `/tmp`
- CI token is limited to `contents: read`
- SAST, dependency, and image vulnerability scanning run on changes

See [SECURITY.md](SECURITY.md) and [docs/THREAT_MODEL.md](docs/THREAT_MODEL.md).

## Roadmap

- [ ] Kubernetes manifests with security contexts and resource limits
- [ ] SBOM generation
- [ ] Image signing / provenance
- [ ] IaC scanning
- [ ] Disposable deployment stage
- [ ] Structured logs and observability

## Author

**Emil Alizada**  
Cybersecurity · DevOps · Secure Backend Engineering
