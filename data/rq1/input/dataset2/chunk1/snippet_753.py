#Source: https://stackoverflow.com/questions/43901079/typeerror-cant-concat-bytes-to-str-python3
request_body = {'grant_type':'password','username': username,'password': password}
request_headers = {'Content-Type' : 'application/x-www-form-urlencoded','Authorization': "hash string"}
http = urllib3.PoolManager()
response = http.request('POST', 'https://api/url/endpoint', headers=request_headers, body=request_body)