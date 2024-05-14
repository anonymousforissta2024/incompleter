import csv
print('Write dictionaries to a CSV file:')
fw = open('test.csv', 'w', newline='')
writer.writeheader()
writer.writerow({'Name': 'Jasmine Barrett', 'Class': 'V'})
writer.writerow({'Name': 'Garry Watson', 'Class': 'V'})
writer.writerow({'Name': 'Courtney Caldwell', 'Class': 'VI'})
fw.close()
fr = open('test.csv', 'r')
csv = csv.reader(fr, delimiter=',')
for row in csv:
    print(row)
fr.close()