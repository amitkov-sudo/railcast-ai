# Architecture

`railcast-ai` follows a modular architecture:

- ingestion pipelines collect GTFS static and realtime feeds
- transform pipelines create model-ready features
- ML workflows train and evaluate delay models
- APIs expose operational and inference endpoints
- Airflow orchestrates scheduled data and training jobs
