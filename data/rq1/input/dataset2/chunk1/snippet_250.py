#Source: https://stackoverflow.com/questions/69766838/scheduling-airflow-taskgroup-throws-attributeerror
def get_task_group(dag, task_group):
    t1 = DummyOperator(task_id='t1', dag=dag, task_group=task_group)
    t2 = DummyOperator(task_id='t2', dag=dag, task_group=task_group)
    t3 = DummyOperator(task_id='t3', dag=dag, task_group=task_group)
    t4 = DummyOperator(task_id='t4', dag=dag, task_group=task_group)
    t5 = DummyOperator(task_id='t5', dag=dag, task_group=task_group)
    t_list = [t2, t3, t4]
    t1.set_downstream(t_list)
    t5.set_upstream(t_list)


with DAG('some_dag', default_args=args) as dag:
    with TaskGroup(group_id=f"run_model_tasks", dag=dag) as tg:
      run_model_task_group = get_task_group(dag, tg)

    a1 = DummyOperator(task_id='a1', dag=dag)
    a2 = DummyOperator(task_id='a2', dag=dag)
    a3 = DummyOperator(task_id='a3', dag=dag)
    a4 = DummyOperator(task_id='a4', dag=dag)

    a1.set_downstream(a2)
    a2.set_downstream(run_model_task_group)
    a3.set_upstream(run_model_task_group)
    a3.set_downstream(a4)