from pprint import pprint
pprint(dict_nums)
print(dict_nums['x'][4])
print(dict_nums['y'][4])
print(dict_nums['z'][4])
for k, v in dict_nums.items():
    print(k, 'has value', v)