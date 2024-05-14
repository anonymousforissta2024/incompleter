#Source: https://stackoverflow.com/questions/66003120/airflow-2-0-attributeerror-myoperator-object-has-no-attribute-kwargs
from datetime import timedelta

from airflow import DAG
from airflow.utils.dates import days_ago
from operators.custom import MyOperator

args = {
    'owner': 'airflow',
}

with DAG(
    dag_id='ex_operator',
    default_args=args,
    schedule_interval='0 0 * * *',
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60)
) as dag:

    custom_ops = MyOperator(
        task_id = 'myop_id',
        name = 'me',
        params = {
            'lib': 'rainy'
        }
    )