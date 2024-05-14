from collections import Counter

def compare_lists(x, y):
    return Counter(x) == Counter(y)
n2 = [30, 20, 10, 30, 20, 50]
print(compare_lists(n1, n2))