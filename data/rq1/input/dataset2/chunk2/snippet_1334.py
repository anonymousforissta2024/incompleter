#Source: https://stackoverflow.com/questions/54858344/python-error-attributeerror-nonetype-object-has-no-attribute-text
import warnings
import requests
from colorama import init
init(autoreset=True)

from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter("ignore", UserWarning)
warnings.simplefilter('ignore', InsecureRequestWarning)

from bs4 import BeautifulSoup as BS


with open('ips.txt','r') as urls:
    for url in urls.readlines():
        req = url.strip()
        try:
            page=requests.get(req, verify=False, allow_redirects=False, stream=True, timeout=10)
            soup = BS(page.text)

            print('\033[32m' + req + ' - Title: ', soup.find('title').text)
        except requests.RequestException as e:
            print('[!] Timeout!')