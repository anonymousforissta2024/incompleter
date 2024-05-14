#Source: https://stackoverflow.com/questions/40929221/typeerror-received-when-using-microsoft-cognitive-computer-vision-api-in-python
import http.client, urllib.request, urllib.parse, urllib.error, base64

MICROSOFT_CV_SUBSCRIPTION_KEY='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

headers = {
   # Request headers
   'Content-Type': 'application/json',
   'Ocp-Apim-Subscription-Key': MICROSOFT_CV_SUBSCRIPTION_KEY,
}

params = urllib.parse.urlencode({
   'visualFeatures': 'Categories,Adult,Faces,Description,ImageType',
   'details': 'Celebrities',
   'language': 'en',
})

data = {
    'url':'http://img.wennermedia.com/article-leads-vertical-300/1250530894_brad_pitt_290x402.jpg',
}

try:
    conn = http.client.HTTPSConnection('api.projectoxford.ai')
    conn.request("POST", "/vision/v1.0/analyze?%s" % params, data, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))