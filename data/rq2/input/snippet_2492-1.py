flatten = lambda l: sum(map(flatten, l), []) if isinstance(l, list) else [l]
print(flatten(a))