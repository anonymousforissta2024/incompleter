#Source: https://stackoverflow.com/questions/62173029/receiving-typeerror-nonetype-object-is-not-subscriptable-at-random-in-python3
import requests
import json
import urllib.request as request
from urllib.request import Request, urlopen
import time

# THINGS
'''
international API: https://arsonwarehouse.com/api/v1/foreign-stock
domestic API: https://api.torn.com/market/  ?selections=itemmarket&key=KEY
personal API: https://api.torn.com/user/2519609?selections=money&key=KEY
'''

capacity = 21
moneyOverride = False
totalCost: int
totalIncome: int

#Takes in the cost per item, multiplies by capacity, returns true if it's affordable
def checkAfford(costPer):
    global totalCost
    totalCost = capacity * costPer
    if totalCost < money:
        return True
    else:
        return False

#Puts together the API link with the ID number and calls pullJSON()
def checkDomestic(id):
    jsonPULL = pullJSON(f"https://api.torn.com/market/{id}?selections=itemmarket&key=YET")
    if jsonPULL == None:
        print("error")
    else:
        return jsonPULL

#Requests the JSON from the server
def pullJSON(url):
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    with urlopen(req) as response:
        if response.getcode() == 200:
           source = response.read()
           data = json.loads(source)
           return data
        else:
           print('An error occurred while attempting to retrieve data from the API.')

internationalData = pullJSON("https://arsonwarehouse.com/api/v1/foreign-stock")
personalData = pullJSON("https://api.torn.com/user/2519609?selections=money&key=YET")
domesticData = checkDomestic(10)

#Money override
if moneyOverride == False:
    money = personalData.get("money_onhand")
else: 
    money = 1000000000000000

print("onhand:", money)

i = 0 

length = len(internationalData["items"])
print(length)

for x in internationalData["items"]:
    time.sleep(0.5)
    ident = x["item_id"]
    domPrice = x["price"]
    print("DOMESTIC:          ID:", ident, " at price:", domPrice)
    domestic = checkDomestic(ident).get("itemmarket")[1]
    inPrice = domestic["cost"]
    if inPrice == None:
        print("error", domestic["ID"])
    location = x["country"]
    print("INTERNATIONAL:     ID:", ident, " at price:", inPrice, "location: ", location)

print("end")