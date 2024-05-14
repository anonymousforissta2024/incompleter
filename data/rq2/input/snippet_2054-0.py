print('The original list is : ' + str(test_list))
res = sorted(test_list, key=lambda sub: (-sub[0], sub[1]))
print('The tuple after custom sorting is : ' + str(res))