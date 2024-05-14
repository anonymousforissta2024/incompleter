#Source: https://stackoverflow.com/questions/53282885/python-adding-values-to-a-dictionary-typeerror-string-indices-must-be-integers
from kafka import KafkaConsumer
import json
import csv
import sys
from datetime import datetime
import os

# connect to kafka topic
kaf = KafkaConsumer('students.all.events')


outputfile = 'C:\\Users\\Documents\\students_output.csv'

outfile = open(outputfile, mode='w', newline='')
master_key = ['id', 'name', 'lastName', 'science', 'math', 'english']

writer = csv.DictWriter(outfile, master_key, delimiter="|")
writer.writeheader()
'''
writer = csv.writer(outfile)
writer.writerow(['JSON_Data'])
'''

i = 1
for row in kaf:
    if i < 5000:
        json_row = json.loads(row.value)
        print('Row: ', i)
        print(json_row)

        dict = {'id': json_row['id'], 'name': json_row['name'], 'lastName': json_row['lastName']}

        for value in json_row['grades']:
            if value['science'] is not None:
                dict['science'] = value['science']
                dict['math'] = value['math']

            elif value['english'] is not None:
                dict['english'] = value['english']

        writer.writerow(dict)
        i += 1
    else:
        break

outfile.close()