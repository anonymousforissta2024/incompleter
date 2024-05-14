from collections import Counter

def compare_lists(x, y):
    return Counter(x) == Counter(y)
n1 = [20, 10, 30, 10, 20, 30]
print(compare_lists(n1, n2))