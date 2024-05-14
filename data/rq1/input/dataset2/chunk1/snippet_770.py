#Source: https://stackoverflow.com/questions/51445557/celery-workflow-error-typeerror-unsupported-operand-types-for-asyncresul
import os
from celery import Celery, group, chord, chain

class CeleryConfig:
    """
    Configuration for Celery
    """
    broker_url = os.environ.get('CELERY_BROKER_URL','mongodb://localhost:9001/jobs')
    result_backend = os.environ.get('CELERY_RESULT_BACKEND', 'mongodb://localhost:9001/')
    celery_mongodb_backend_settings = {
        "database": "results", 
        "taskmeta_collection": "test",
    }
    enable_utc = True
    timezone = "UTC"
    celery_imports = ('test',)
    task_always_eager = os.environ.get('CELERY_ALWAYS_EAGER', False)
    task_eager_propagates = os.environ.get('CELERY_EAGER_PROPAGATES',False)
    task_serializer = 'json'

celery_app = Celery("test")
celery_app.config_from_object(CeleryConfig)

@celery_app.task(bind=True)
def dummy_task(self, *args, **kwargs):
    return True

@celery_app.task(bind=True)
def a(self, pagination, *args, **kwargs):
    return pagination[0] + pagination[1]

@celery_app.task(bind=True)
def b(self, pagination, *args, **kwargs):
    return pagination[0] + pagination[1]

@celery_app.task(bind=True)
def workflow(self):
    batch_size = 10
    flow_a = chord(group(a.s((k,batch_size), max_retries=None) for k in range(5)), dummy_task.s())()
    flow_b = chord(group(b.si((k,batch_size), immutable=True, max_retries=None) for k in range(5)), dummy_task.s())()

    r = chain(flow_a, flow_b)()
    return r

task = workflow.apply_async()