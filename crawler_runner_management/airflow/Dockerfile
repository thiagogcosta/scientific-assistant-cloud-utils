FROM apache/airflow:slim-2.9.2-python3.10 AS airflow

RUN python3 -m pip install --upgrade pip wheel setuptools && \
    python3 -m pip cache purge

COPY requirements.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements.txt && \
    python3 -m pip cache purge

ENV AIRFLOW_HOME=/opt/airflow

EXPOSE 8080

ENTRYPOINT "airflow" "standalone"