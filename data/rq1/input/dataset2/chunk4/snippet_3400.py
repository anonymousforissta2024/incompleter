#Source: https://stackoverflow.com/questions/67422146/attributeerror-module-urllib-response-has-no-attribute-status-code
import datetime
import urllib.request
import urllib
import requests

url = "https://ubisoftconnect.com/en-US/profile/"
response = urllib.response.status_code("https://ubisoftconnect.com/en-US/profile/")

print(r.status_code)

url = 'https://ubisoftconnect.com/en-US/profile/'
available = "available.txt"
users = "usernames.txt"
now = datetime.datetime.now ()
if response.status_code == 200:
    print('Available')
elif response.status_code == 404:
    print('Unavailable')


def initialize():
    ascii_banner = pyfiglet.figlet_format("Made  By  Gxzs!!")
    print(ascii_banner)
    print(f"{count()} usernames detected")
    print("Press ENTER to begin checking")
    input("")
    check()