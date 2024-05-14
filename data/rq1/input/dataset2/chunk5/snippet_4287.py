#Source: https://stackoverflow.com/questions/57095785/how-to-fix-typeerror-while-trying-to-find-a-tag-using-xml-etree
import xml.etree.ElementTree as ET
import ssl
import urllib.error, urllib.parse, urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

service_url = 'http://www.geoplugin.net/xml.gp?'
ip_api = 'https://api.ipify.org'

ip_addr = urllib.request.urlopen(ip_api, context=ctx).read().decode() 
parms = dict()
parms['ip'] = ip_addr
url = service_url + urllib.parse.urlencode(parms)
print('Retrieving:',url)

xmldat = urllib.request.urlopen(url, context=ctx).read().decode()
print('Retrieved', len(xmldat), 'characters' )
print(xmldat)
tree = ET.fromstring(xmldat)

region = tree.find('geoplugin_region').text()
country = tree.find('geoplugin_countryName').text()
latitude = tree.find('geoplugin_latitude').text()
longitude = tree.find('geoplugin_longitude').text()
currency_exchange = tree.find('geoplugin_currencyConverter').text()

print('Region:', region, '\nCountry:', country, '\nLatitude', latitude, '\nLongitude:', longitude, '\nCurrency Exchange Rate (relative to US Dollar)', currency_exchange)