#Source: https://stackoverflow.com/questions/56976222/typeerror-tuple-indices-must-be-integers-or-slices-not-dict
tax_rates = {
  'AB' : .05,
  'BC' : .12,
  'MN' : .13,
  'NB' : .15,
  'NL' : .15,
  'NT' : .05,
  'NS' : .15,
  'ON' : .13,
  'PE' : .15,
  'QC' : .1475,
  'ST' : .11,
  'YK' : .05
},

for key in tax_rates:
  print(tax_rates[key])

for key in tax_rates.items():
  print(key)

for value in tax_rates.items():
  print(value)

for key,value in tax_rates.items():
  print(key,value)

tax = tax_rates.keys()
print(tax)