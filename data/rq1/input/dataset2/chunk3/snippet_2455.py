#Source: https://stackoverflow.com/questions/56970332/attributeerror-lxml-etree-qname-object-has-no-attribute-resolve
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep import Client, Settings
from zeep.cache import SqliteCache
from zeep.transports import Transport

from conf.shared_vars import B2B_PROXY, WSDL_PROXY

session = Session()
session.auth = HTTPBasicAuth(B2B_PROXY['key'], B2B_PROXY['secret'])
wsdl = WSDL_PROXY + "SomeServices.wsdl"

client = Client(
    wsdl=wsdl, 
    transport=Transport(
        session=session, 
        cache=SqliteCache(path='./sqlite.db')))