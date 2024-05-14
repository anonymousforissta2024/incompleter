import requests
print('Parameters: ', payload)
r = requests.get('https://httpbin.org/get', params=payload)
print('Print the url to check the URL has been correctly encoded or not!')
print(r.url)
print('\nPass a list of items as a value:')
payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
print('Parameters: ', payload)
r = requests.get('https://httpbin.org/get', params=payload)
print('Print the url to check the URL has been correctly encoded or not!')
print(r.url)