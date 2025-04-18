# Airflow DAG for batch ETL (optional)
from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'retail_etl',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False
)

etl_task = BashOperator(
    task_id='run_etl_script',
    bash_command='echo "ETL job would run here"',
    dag=dag
)

etl_task