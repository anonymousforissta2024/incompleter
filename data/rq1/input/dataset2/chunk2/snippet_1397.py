#Source: https://stackoverflow.com/questions/70557651/typeerror-using-pprint-on-counter-objects-that-have-been-updated-bit-of-an-ed
try:
    pprint(intcounter, sort_dicts=False)
except TypeError as t:
    print(t)