print('The original list is : ' + str(test_list))
i, j = (2, 3)
res = [sub for sub in test_list if len(sub) >= i and len(sub) <= j]
print('The tuple list after filtering range records : ' + str(res))