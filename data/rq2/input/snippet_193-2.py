def cast_list(val):
    return list(val) if isinstance(val, (tuple, list, set, dict)) else [val]
d1 = [1]
print(type(d1))
print(cast_list(d1))
print(type(d2))
print(cast_list(d2))
d3 = {'Red', 'Green'}
print(type(d3))
print(cast_list(d3))
d4 = {1: 'Red', 2: 'Green', 3: 'Black'}
print(type(d4))
print(cast_list(d4))