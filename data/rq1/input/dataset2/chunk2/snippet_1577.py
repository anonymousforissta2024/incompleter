#Source: https://stackoverflow.com/questions/75893246/python-prefect-2-9-0-typeerror-fn-must-be-callable
@task
def print_values():
    print("Test 1: "+ datetime.now().strftime("%H:%M:%S"))

with Flow("my-flow") as flow:
    print_values()

flow.run_config(
    {"scheduler": IntervalSchedule(interval=timedelta(seconds=10))}
)