#Source: https://stackoverflow.com/questions/40535615/python-typeerror-with-for-logic-iterating-data-values
import json
import csv

with open('C:\\folder\\dev\\TagAlarms.txt',"r") as file:
    data = json.load(file)

with open('C:\\folder\\dev\\TagAlarms.csv',"w",newline='') as file:
    csv_file = csv.writer(file)
    for dev in data["devs"]:
        for tag in dev["tags"]:
            for alarm in tag["alarmst"]:
                csv_file.writerow(alarm['dateStatus'],[alarm['dateStart'], alarm['status'], alarm['type']])