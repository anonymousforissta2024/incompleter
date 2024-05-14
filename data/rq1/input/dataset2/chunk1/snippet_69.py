#Source: https://stackoverflow.com/questions/63920923/getting-error-typeerror-create-task-takes-from-1-to-2-positional-arguments-bu
from google.cloud import tasks_v2

import json


GCP_PROJECT='test'
GCP_LOCATION='europe-west6'


def enqueue_task(queue_name, payload, process_url):
  client = tasks_v2.CloudTasksClient()
  parent = client.queue_path(GCP_PROJECT, GCP_LOCATION, queue_name)

  task = {
    'app_engine_http_request': {
      'http_method': 'POST',
      'relative_uri': process_url
    }
  }

  if payload is None:
    return False

  payload = json.dumps(payload)
  converted_payload = payload.encode()

  task['app_engine_http_request']['body'] = converted_payload
  return client.create_task(parent, task)