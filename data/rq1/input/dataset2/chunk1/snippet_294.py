#Source: https://stackoverflow.com/questions/69766838/scheduling-airflow-taskgroup-throws-attributeerror
a2.set_downstream(run_model_task_group)
a3.set_upstream(run_model_task_group)