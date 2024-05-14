#Source: https://stackoverflow.com/questions/64342038/attributeerror-int-object-has-no-attribute-weight
from converters import KgLbs as kglbs

weight = int(input("Weight: "))
weight = kglbs.kg_to_lbs(weight)
print(weight)