#Source: https://stackoverflow.com/questions/33792582/typeerror-getresponse-got-an-unexpected-keyword-argument-buffering
import requests 
from requests_file import FileAdapter

s = requests.Session() 
s.mount('file://', FileAdapter()) 
resp = s.get('file:///local_package_name') 
urldst = 'Upload URL' 
rdst = requests.post(urldst, files={'filename': resp.content}) 
print(rdst)