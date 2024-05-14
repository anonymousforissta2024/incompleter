from collections import Counter
print('The original dictionary : ' + str(test_dict))
cnt = Counter()
for idx in test_dict.values():
    cnt.update(idx)
res = {idx: [key for key in j if cnt[key] == 1] for idx, j in test_dict.items()}
print('Uncommon elements records : ' + str(res))