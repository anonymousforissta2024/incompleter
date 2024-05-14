from collections import defaultdict
print('The original dictionary is : ' + str(test_dict))
res = defaultdict(list)
for key, val in test_dict.items():
    for ele in val:
        res[ele].append(key)
print('The values associated dictionary : ' + str(dict(res)))