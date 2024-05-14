#Source: https://stackoverflow.com/questions/61955009/typeerror-not-all-arguments-converted-during-string-formatting-data-upload-to
import time
import requests

temp = [12,13,14,15,16,17,18,19,12,10]
humi = [67,68,69,50,56,57,59,59,45,48]

for x in range(10):
    print ('Uploading sample',x,'...')
    resp=requests.get('https://api.thingspeak.com/update?api_key=WTJJF5W2CL8IGT19&field1=0' %(temp[x],humi[x]))
    time.sleep(20)