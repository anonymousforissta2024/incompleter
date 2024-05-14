from collections import Counter
l2 = [1, 1, 2, 4, 5, 6]
print('Original lists:')
c1 = Counter(l1)
c2 = Counter(l2)
diff = c1 - c2
print(list(diff.elements()))