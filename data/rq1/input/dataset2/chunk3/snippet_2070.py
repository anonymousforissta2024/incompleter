#Source: https://stackoverflow.com/questions/61365330/celery-running-signature-from-database-attributeerror-object-has-no-attribute
def example_job_1(arg_1, arg_2, **kwargs):
    example_task_1_s = task_1.si(arg_1)
    example_task_2_s = task_2.s(arg_2)
    return example_task_1_s | example_task_2_s

def example_job_2(arg_1, arg_2, **kwargs):
    return task_1.si(arg_1)


signature = example_job_1(arg_1, arg_2) | example_job_2(arg_1) # _chain object