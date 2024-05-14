#Source: https://stackoverflow.com/questions/64644096/typeerror-module-object-is-not-callable-python3
from modules import HTTPHeaders
site = "https://google.com"
HTTPHeaders(site, _verbose=True)