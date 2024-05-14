import csv
with open('temp.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(data)
with open('temp.csv', newline='') as csvfile:
    data = csv.reader(csvfile, delimiter=' ')
    for row in data:
        print(', '.join(row))