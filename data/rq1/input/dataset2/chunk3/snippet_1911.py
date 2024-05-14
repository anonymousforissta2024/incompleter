#Source: https://stackoverflow.com/questions/66557452/google-indexing-api-batch-request-attributeerror-resource-object-has-no-attri
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.http import BatchHttpRequest
import httplib2
from googleapiclient.discovery import build 
SCOPES = [ "https://www.googleapis.com/auth/indexing" ]
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"

# service_account_file.json is the private key that you created for your service account.
JSON_KEY_FILE = "service_account_file.json"

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)

service = build('indexing', 'v3', credentials=credentials)

def insert_event(request_id, response, exception):
    if exception is not None:
      print(exception)
    else:
      print(response)

batch = BatchHttpRequest(callback=insert_event)
batch.add(service.events().quickAdd(url="URL HERE", type="URL_UPDATED"))
batch.add(service.events().quickAdd(url="URL HERE", type="URL_UPDATED"))
batch.execute(http=http)