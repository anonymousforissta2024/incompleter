#Source: https://stackoverflow.com/questions/70557651/typeerror-using-pprint-on-counter-objects-that-have-been-updated-bit-of-an-ed
try:
    intcounter.update({"Hello": "World"})
except TypeError as t:
    print(t)