from collections import Counter
d2 = {'a': 300, 'b': 200, 'd': 400}
d = Counter(d1) + Counter(d2)
print(d)