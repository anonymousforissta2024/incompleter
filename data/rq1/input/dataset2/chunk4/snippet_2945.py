#Source: https://stackoverflow.com/questions/65881771/typeerror-cant-concat-str-to-bytes-for-google-indexing-api
from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json
import pandas as pd

SCOPES = "https://www.googleapis.com/auth/indexing"
ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
JSON_KEY_FILE = "river-formula-BLABLA.json"

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())
content = {"url":"https://www.parmalat.it/chef/ricette/cannelloni-al-ragu","type":"URL_UPDATED"}

response, content=http.request(ENDPOINT, method="POST", body=content)

print(response)
print(content)