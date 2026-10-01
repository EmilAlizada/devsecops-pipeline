# Architecture

This repository keeps the application intentionally small so the complete DevSecOps feedback loop stays easy to inspect.

## Runtime

```text
Client -> Django/Gunicorn -> PostgreSQL
```

Docker Compose starts an unprivileged Django application container and PostgreSQL. The app container is read-only and uses temporary `/tmp` storage.

## CI

```text
Git push / PR
  -> Ruff
  -> Django checks
  -> Pytest
  -> Bandit
  -> pip-audit
  -> Docker build
  -> Trivy image scan
```

The GitHub Actions workflow has read-only repository permissions. Secrets and environment-specific values are not committed.
