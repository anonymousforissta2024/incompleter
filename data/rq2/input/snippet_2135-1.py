from collections import defaultdict
print('The original list : ' + str(test_list))
res = defaultdict(list)
for ele in test_list:
    res[ele].append(ele)
print('Similar grouped dictionary : ' + str(dict(res)))