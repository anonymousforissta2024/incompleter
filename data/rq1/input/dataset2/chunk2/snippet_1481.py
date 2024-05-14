#Source: https://stackoverflow.com/questions/50416692/typeerror-request-missing-1-required-positional-argument-url
import urllib3

http = urllib3.PoolManager(10)
url = 'https://www.desertessence.com/sitemap.xml'

pagedata = http.request(url).data