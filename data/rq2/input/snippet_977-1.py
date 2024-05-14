from collections import defaultdict
d = defaultdict(list)
for k, v in class_roll:
    d[k].append(v)
print(sorted(d.items()))