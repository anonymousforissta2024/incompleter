#Source: https://stackoverflow.com/questions/48677298/getting-this-error-typeerror-list-indices-must-be-integers-or-slices-not-str
records = []

for result in links:
    url = links['href']
    records.append(url)