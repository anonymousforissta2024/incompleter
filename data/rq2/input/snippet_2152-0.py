import csv
with open('my_csv.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')
    writer.writerows(marks)
with open('my_csv.csv', newline='') as file:
    reader = csv.reader(file, quoting=csv.QUOTE_NONNUMERIC, delimiter=' ')
    output = []
    for row in reader:
        output.append(row[:])
for rows in output:
    print(rows)