from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator

from pipelines.ingestion.gtfs_realtime_ingest import run as ingest_realtime
from pipelines.ingestion.gtfs_static_ingest import run as ingest_static
from ml.training.train import train_model


with DAG(
    dag_id="train_delay_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule="@daily",
    catchup=False,
    tags=["railcast", "ml", "gtfs"],
) as dag:
    task_ingest_static = PythonOperator(task_id="ingest_gtfs_static", python_callable=ingest_static)
    task_ingest_realtime = PythonOperator(task_id="ingest_gtfs_realtime", python_callable=ingest_realtime)
    task_train = PythonOperator(task_id="train_model", python_callable=train_model)

    [task_ingest_static, task_ingest_realtime] >> task_train
