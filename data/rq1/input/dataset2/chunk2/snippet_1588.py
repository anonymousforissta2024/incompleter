#Source: https://stackoverflow.com/questions/44934948/typeerror-list-indices-must-be-integers-or-slices-not-str-get-from-json
import urllib.parse
import requests

raw_json = 'http://live.ksmobile.net/live/getreplayvideos?userid='
print()

userid = 735890904669618176
#userid = input('UserID: ')

url = raw_json + urllib.parse.urlencode({'userid=': userid}) + '&page_size=1000'
print(url)

json_data = requests.get(url).json()
print()


for coordinates in json_data['data']['video_info']:
    print(coordinates['lat'], coordinates['lnt'])
    print()