from collections import Counter
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
l2 = [1, 1, 2, 4, 5, 6]
print('Original lists:')
c2 = Counter(l2)
diff = c1 - c2
print(list(diff.elements()))