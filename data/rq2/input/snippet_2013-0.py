print('The original list is : ' + str(test_list))
K = 3
res = []
for idx, ele in enumerate(test_list):
    if (idx + 1) % K == 0:
        res.append(list(reversed(ele)))
    else:
        res.append(ele)
print('After reversing every Kth row: ' + str(res))