from collections import defaultdict

def test(*dicts):
    result = defaultdict(list)
    for el in dicts:
        for key in el:
            result[key].append(el[key])
    return dict(result)
d1 = {'w': 50, 'x': 100, 'y': 'Green', 'z': 400}
print('Original dictionaries:')
print(d1)
print(d2)
print('\nCombined dictionaries, creating a list of values for each key:')
print(test(d1, d2))