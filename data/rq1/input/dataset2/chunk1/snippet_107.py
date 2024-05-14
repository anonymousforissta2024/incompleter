#Source: https://stackoverflow.com/questions/53332704/xcom-pull-returns-a-nameerror-on-ti
default_args = {
    'owner': 'me',
    'start_date': dt.datetime(2017, 10, 30),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=10),
    'provide_context' : True,
}



def get_last_date(**kwargs):
    kwargs['ti'].xcom_push(key='last_date', value='2018-11-15')
    return True



with DAG('ga_mysql_dag2',
         default_args=default_args,
         schedule_interval=None,
         catchup=False,
         ) as dag:

    last_date_task = PythonOperator(task_id='last_date_task', python_callable=get_last_date, provide_context=True)

    ga_wh_task = GoogleAnalyticsReportingToMySqlOperator(task_id='ga_wh_task', google_analytics_conn_id='google_analytics', key_file=key_file,\
                                        view_id=view_id, until=until, dimensions=dimensions, metrics=metrics, database=database,\
                                        table = table, mysql_conn_id = mysql_conn_id,
                                        provide_context=True, since={{ti.xcom_pull(task_ids="last_date_task", key='last_date')}})
    sleep = BashOperator(task_id='sleep', bash_command='sleep 10')

# Dependencies
last_date_task >> ga_warehouse_task >> sleep