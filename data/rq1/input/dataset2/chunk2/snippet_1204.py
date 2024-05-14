#Source: https://stackoverflow.com/questions/33022424/typeerror-str-does-not-support-the-buffer-interface-python-3-4-conversion
from base64 import b64encode

username = 'manager'
password = 'test.manager'

headers = {"Authorization": " Basic " + b64encode(username + ":" + password), "Content-Type": "application/json"}