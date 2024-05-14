#Source: https://stackoverflow.com/questions/48374582/rest-api-post-request-causing-attributeerror-bytes-object-has-no-attribute-i
from urllib.request import Request, urlopen
from urllib.parse import urlencode

headers = {
  'Content-Type':'application/json',
  'X-API-KEY':'mykey',
  'X-API-SECRET':'mysecretkey'
}

values = {
"exchange_code": "BINA",
"exchange_market": "BTC/USDT",
"type": "all"
}


values = urlencode(values).encode("utf-8")
headers = urlencode(headers).encode("utf-8")


request = Request('https://api.coinigy.com/api/v1/data', data=values, headers=headers)
response_body = urlopen(request,values).read()
print(response_body)