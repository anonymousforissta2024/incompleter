#Source: https://stackoverflow.com/questions/40535615/python-typeerror-with-for-logic-iterating-data-values
import json
import csv

with open('C:\\folder\\dev\\Tags.txt',"r") as file:
    data = json.load(file)

with open('C:\\folder\\dev\\Tags.csv',"w",newline='') as file:

    csv_file = csv.writer(file)
    for dev in data["devs"]:
        for tag in dev["tags"]:
            csv_file.writerow([tag['id'], tag['name'], tag['dataType'], tag['description'], tag['alarm'], tag['value'], tag['quality'], tag['DevTagId']])