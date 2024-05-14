print('The original list is : ' + str(test_list))
res = {idx + 1: test_list[idx] for idx in range(len(test_list))}
print('The constructed dictionary : ' + str(res))