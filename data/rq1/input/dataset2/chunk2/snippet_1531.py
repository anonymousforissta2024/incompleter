#Source: https://stackoverflow.com/questions/54735075/typeerror-a-bytes-like-object-is-required-not-str-when-using-rest-in-python
import requests, base64

usrPass = "user:pass"
b64Val = base64.b64encode(usrPass)
api_URL = 'api-url'
r=requests.post(api_URL, 
                headers={"Authorization": "Basic %s" % b64Val},
                data=payload)