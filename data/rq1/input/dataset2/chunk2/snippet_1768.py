#Source: https://stackoverflow.com/questions/70372223/trying-to-figure-this-error-attributeerror-int-object-has-no-attribute-keys
data_keys = list(range(-5, -11, -1))
result = {}

for element in data_keys:
    result[element] = random()

sorted_values = collections.OrderedDict(sorted(result.items(), key=lambda t: t[1]))

pprint(sorted_values)

d = dict(sorted_values)
pprint(d)

with open('ordered-values.csv', 'w', newline='') as file:
    fieldnames = ['keys', 'values']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    for data in d:
        writer.writerow(data)