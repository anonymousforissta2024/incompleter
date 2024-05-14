import csv
csv_string = '1,2,3\n4,5,6\n7,8,9\n'
print('Original string:')
print(csv_string)
print('List of CSV formatted strings:')
print(lines)
reader = csv.reader(lines)
parsed_csv = list(reader)
print('\nList representation of the CSV file:')
print(parsed_csv)