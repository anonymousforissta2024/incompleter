#Source: https://stackoverflow.com/questions/72849402/api-error-typeerror-string-indices-must-be-integers
import json
import requests
import configuration
url = 'https://client.blutudlut.xyz/api/application/servers'
headers = {
    "Authorization": "Bearer "+ configuration.pterodactyl_admin_api,
    "Accept": "application/json",
    "Content-Type": "application/json",
}

response = requests.request('GET', url, headers=headers)
print(response.text)
json_str = json.dumps(response.text)
resp = json.loads(json_str)
print(resp)
print(resp['data'])