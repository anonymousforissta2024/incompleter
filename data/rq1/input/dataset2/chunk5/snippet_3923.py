#Source: https://stackoverflow.com/questions/54948165/working-with-json-api-data-and-getting-typeerror-list-indices-must-be-integers
import requests
import csv
import re

outputfile = 'file.csv'
outfile = open(outputfile, mode='w', newline='')

master_key = ['name', 'address', 'phoneNumber']

writer = csv.DictWriter(outfile, master_key, delimiter=",")
writer.writeheader()

with open('idfile.csv') as csv_file:
    open_file = csv.reader(csv_file, delimiter=',')
    for row in open_file:
        for id in row:
            url = "https://schoolsite/studentIds/"
            response = requests.get(url)
            data = response.json()
            print(data)
            dict = {'name': data['input']['name'], 'address' : data['input']['address'], 'phoneNumber' : data['input']['phoneNumber']}
            writer.writerow(dict)