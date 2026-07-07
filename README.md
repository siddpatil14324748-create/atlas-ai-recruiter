# Atlas AI Recruiter

Production-grade backend foundation for Atlas AI, with AI Recruiter as the first module.

## What is included

- FastAPI application with a health endpoint
- Async-ready architecture structured for Clean Architecture and DDD
- PostgreSQL and Redis support through Docker Compose
- SQLAlchemy 2.x and Alembic migration scaffold
- Environment-based configuration with Pydantic Settings
- Structured JSON logging
- Pytest, Ruff, Black, and pre-commit setup

## Repository structure

```text
atlas-ai-recruiter/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── core/
│   │   ├── ai/
│   │   ├── memory/
│   │   ├── integrations/
│   │   ├── scheduler/
│   │   ├── domain/
│   │   ├── database/
│   │   ├── workers/
│   │   ├── modules/
│   │   └── main.py
│   ├── tests/
│   ├── pyproject.toml
│   └── requirements.txt
├── infrastructure/
├── docs/
├── scripts/
├── .env.example
├── docker-compose.yml
├── Dockerfile
├── .pre-commit-config.yaml
└── README.md
```

## Getting started

1. Copy the environment template:
   ```bash
   cp .env.example .env
   ```

2. Start the services with Docker Compose:
   ```bash
   docker compose up --build
   ```

3. Open the API documentation:
   - http://localhost:8000/docs
   - http://localhost:8000/api/v1/health

## Local development

```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Run tests:

```bash
pytest
```

Run linting and formatting:

```bash
ruff check .
black .
```
