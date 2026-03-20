FROM apache/airflow:2.9.3-python3.11

WORKDIR /opt/airflow
COPY airflow /opt/airflow/airflow
COPY pipelines /opt/airflow/pipelines
COPY ml /opt/airflow/ml
