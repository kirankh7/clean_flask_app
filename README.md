# clean_flask_app

A modernized Flask application using the app-factory pattern with modular blueprints, env-based config, and a Claude AI endpoint.

## Quick Start

```bash
cp .env.example .env
pip install -r requirements.txt
python run.py
```

## Docker

```bash
docker build -t clean_flask_app .
docker run -p 8000:8000 --env-file .env clean_flask_app
```

## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `SECRET_KEY` | Yes | Flask secret key |
| `DATABASE_URL` | No | PostgreSQL URL (defaults to SQLite) |
| `FLASK_ENV` | No | `development` or `production` |
| `ANTHROPIC_API_KEY` | No | Enables `/ask` AI endpoint |
| `PORT` | No | Server port (default: 8000) |

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Hello world page |
| `/surnames/?Name=John+Doe` | GET | Parse surname |
| `/health` | GET | Health check with uptime |
| `/diag` | GET | Service diagnostics |
| `/ask` | POST | AI-powered Q&A (Claude) |

## Architecture

```
app/
├── __init__.py      # Application factory
├── config.py        # Env-based config
├── models.py        # SQLAlchemy models
├── hello/           # Main routes blueprint
├── health/          # Health endpoint blueprint
├── diag/            # Diagnostics blueprint
└── ai/              # Claude AI blueprint
```
