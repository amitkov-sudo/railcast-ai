# railcast-ai
Production-style monorepo for train delay prediction using GTFS static and GTFS-realtime data.

## Project Layout

- `services/` - FastAPI backend and model inference services
- `pipelines/` - data ingestion, transforms, shared ETL utilities
- `airflow/` - DAG orchestration and Airflow plugins
- `ml/` - feature logic, training, evaluation, and model artifacts
- `data/` - local raw/processed/external data zones
- `infra/` - Docker and operational scripts
- `frontend/` - React frontend app scaffold
- `docs/` - architecture, contracts, and diagrams
- `tests/` - unit and integration tests

## Quick Start

1. Create a virtual environment and install dependencies:
   - `python -m venv .venv`
   - `source .venv/bin/activate`
   - `pip install -r requirements.txt`
2. Copy `.env.example` to `.env` and edit values.
3. Start services:
   - `docker compose up --build`

## Core Services

- API service: `services/api`
- ML inference service: `services/ml-inference`
