#Source: https://stackoverflow.com/questions/45955106/why-do-i-get-an-attributeerror-on-str-sort
bands = []
band = []
headline = input('Headline: ')
while band != "":
  bands.append(band)
  band = input('Band: ')
band.sort()
print(headline)
for band in bands:
  print(band)