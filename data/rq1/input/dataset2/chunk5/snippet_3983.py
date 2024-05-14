#Source: https://stackoverflow.com/questions/37633031/attributeerror-list-object-has-no-attribute-items
import json
from urllib.request import urlopen, Request
from urllib.parse import urlencode

def sTrackTemperature():
    "Constantly Show an Output of the Track Temperature"
    sDataRaw = urlopen(Request("https://api.samsara.com/v1/sensors/temperature?access_token=", 518, [2]))
    sDataParse = sDataRaw.read().decode('utf-8')
    sDataJson = json.loads(sDataParse)
    return sDataJson;
print(str(sTrackTemperature()))