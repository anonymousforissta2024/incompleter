from collections import defaultdict
class_roll = [('v', 1), ('vi', 2), ('v', 3), ('vi', 4), ('vii', 1)]
for k, v in class_roll:
    d[k].append(v)
print(sorted(d.items()))