def last(n):
    return n[-1]

def sort(tuples):
    return sorted(tuples, key=last)
print('Sorted:')
print(sort(a))