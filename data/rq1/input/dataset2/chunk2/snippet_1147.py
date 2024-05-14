#Source: https://stackoverflow.com/questions/54697609/why-am-i-getting-error-typeerror-string-indices-must-be-integers
import json
from pprint import pprint

with open('driver.json', 'r') as f:
    drivers_dict = json.load(f)

for driver in drivers_dict:
    print(driver['id'])
    print(driver['groupId'])
    print(driver['vehicleId'])
    print(driver['username'])
    print(driver['name'])