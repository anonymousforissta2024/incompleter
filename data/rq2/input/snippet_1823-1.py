print('The original list : ' + str(test_list))
test_list.sort(key=len)
res = []
for idx, val in enumerate(test_list):
    if val not in ', '.join(test_list[idx + 1:]):
        res.append(val)
print('The filtered list : ' + str(res))