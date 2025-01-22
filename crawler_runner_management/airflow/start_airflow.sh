#!/bin/bash
airflow db upgrade

airflow users create \
    --role Admin \
    --username admin \
    --email admin@example.com \
    --firstname Admin \
    --lastname Admin \
    --password admin || echo "Admin user already exists."

airflow scheduler &

exec airflow webserver