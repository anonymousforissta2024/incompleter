#Source: https://stackoverflow.com/questions/63287967/keep-getting-attributeerror-str-object-has-no-attribute-items
response = requests.request("GET", folder_url, headers=headers, data=payload)
jsonResponse = response.json()

for key, value in jsonResponse.items():
                print(key, ":", value)

URL = jsonResponse["presignedUrl"]
processnum = jsonResponse["processId"]

assetupload = requests.request("PUT", URL, headers='Content-Type: image/tiff', data=payload)