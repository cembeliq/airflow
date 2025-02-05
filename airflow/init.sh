#!/bin/bash
airflow db init
airflow users create \
    --username airflow \
    --firstname airflow \
    --lastname airflow \
    --role Admin \
    --email airflow@airflow.com \
    --password airflow
