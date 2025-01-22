from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from datetime import datetime
import os

# DESC: Get the year of the journals
current_year = datetime.now().year
previous_year = current_year - 1
journal_years = [str(current_year), str(previous_year)]

# DESC: Get the numbers of the journals
max_journal_number = os.environ.get('MAX_JOURNAL_NUMBER', '')
journal_numbers = [str(i) for i in range(1, int(max_journal_number))]

default_args = {
   'owner': 'thiagogcosta',
   'depends_on_past': False,
   'start_date': datetime(2025, 1, 1),
   'retries': 0,
   }

# DESC: Get the numbers of the journals
dag = DAG(
    'scientific_assistant_dag',
    schedule_interval='@weekly',
    catchup=False,
    default_args=default_args
)

# DESC: Iterate over the lists of journal years and numbers
crawler_version = os.environ.get('CRAWLER_VERSION', '')
chroma_host = os.environ.get('CHROMA_HOST', '')

for year in journal_years:
   for number in journal_numbers:
      scientific_assistant_crawler = DockerOperator(
         task_id=f'scientific-assistant-crawler-{year}-{number}',
         image=f"thiagogcosta/scientific-assistant-crawler:{crawler_version}",
         container_name='scientific-assistant-crawler',
         docker_url='unix://var/run/docker.sock', 
         mount_tmp_dir=False,
         auto_remove=True,
         environment={
            'JOURNAL_NUMBER': number,
            'JOURNAL_YEAR': year,
            'CHROMA_HOST': chroma_host
         },
         dag=dag,
         network_mode='bridge'
      )