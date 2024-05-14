from collections import Counter
test_dict = {'Manjeet': [1, 4, 5, 6], 'Akash': [1, 8, 9], 'Nikhil': [10, 22, 4], 'Akshat': [5, 11, 22]}
print('The original dictionary : ' + str(test_dict))
for idx in test_dict.values():
    cnt.update(idx)
res = {idx: [key for key in j if cnt[key] == 1] for idx, j in test_dict.items()}
print('Uncommon elements records : ' + str(res))