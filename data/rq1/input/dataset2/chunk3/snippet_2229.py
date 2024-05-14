#Source: https://stackoverflow.com/questions/50603012/python-attributeerror-nonetype-object-has-no-attribute-execute
## Third party Library Imports
import pandas as pd
import psycopg2
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import io

# Following are defaults which can be overridden later on
default_args = {
'owner': 'airflow',
'depends_on_past': False,
'start_date': datetime(2018, 5, 29, 12),
'email': ['airflow@airflow.com']
}

dag = DAG('sample1', default_args=default_args)

## Login to DB

def db_log(**kwargs):
  global db_con
  try:
    db_con = psycopg2.connect(
       " dbname = 'name' user = 'user' password = 'pass' host = 'host' port = '5439'")
  except:
    print("I am unable to connect")
    print('Connection Task Complete')
    task_instance = kwargs['task_instance']
    task_instance.xcom_push(key="dwh_connection" , value = "dwh_connection")
    return (dwh_connection)



t1 = PythonOperator(
  task_id='DWH_Connect',
  python_callable=data_warehouse_login,provide_context=True,
  dag=dag)

#######################

def insert_data(**kwargs):
  task_instance = kwargs['task_instance']
  db_con_xcom = task_instance.xcom_pull(key="dwh_connection", task_ids='DWH_Connect')
  cur = db_con_xcom
  cur.execute("""insert into tbl_1 select limit 2 """)


##########################################

t2 = PythonOperator(
  task_id='DWH_Connect1',
  python_callable=insert_data,provide_context=True,dag=dag)

t1 >> t2