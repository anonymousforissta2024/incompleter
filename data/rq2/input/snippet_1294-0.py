def pluck(lst, key):
    return [x.get(key) for x in lst]
print(pluck(simpsons, 'age'))