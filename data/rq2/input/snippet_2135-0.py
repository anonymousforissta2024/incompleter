from collections import defaultdict
test_list = [4, 6, 6, 4, 2, 2, 4, 4, 8, 5, 8]
print('The original list : ' + str(test_list))
for ele in test_list:
    res[ele].append(ele)
print('Similar grouped dictionary : ' + str(dict(res)))