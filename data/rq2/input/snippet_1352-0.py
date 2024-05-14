import csv
fw = open('test.csv', 'w', newline='')
writer = csv.writer(fw, delimiter=',')
writer.writerow(['a', 'b', 'c'])
writer.writerow(['d', 'e', 'f'])
writer.writerow(['g', 'h', 'i'])
fw.close()
csv = csv.reader(fr, delimiter=',')
for row in csv:
    print(row)
fr.close()