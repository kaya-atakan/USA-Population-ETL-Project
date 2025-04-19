from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from scripts.extract import extract
from scripts.transform import transform
from scripts.viz import visualize

DEFAULT_ARGS = {
    'start_date': datetime(2025, 4, 19),
    'retries': 1
}

dag = DAG(
    dag_id='etl_web_api_pipeline',
    default_args=DEFAULT_ARGS,
    schedule_interval='@daily',
    catchup=False
)

extract_task = PythonOperator(task_id='extract', python_callable=extract, dag=dag)
transform_task = PythonOperator(task_id='transform', python_callable=transform, dag=dag)
visualize_task = PythonOperator(task_id='visualize', python_callable=visualize, dag=dag)

extract_task >> transform_task >> visualize_task