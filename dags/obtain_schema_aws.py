

from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner' : 'angel',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dgraph_test_v1',
    default_args = default_args,
    description='gcp composer',
    start_date=datetime(2023,5,30),
    schedule_interval='@daily'
) as dag:
    task1 = BashOperator(
        task_id='first_task',
        bash_command= "curl -X POST  -H 'Content-Type: application/dql'  http://44.211.75.97:8000/query -d $'schema {}'"   
    )

    task1
    