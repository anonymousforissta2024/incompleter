test_list = ['geekforgeeks', 'is', 'best', 'for', 'geeks']
print('The original list is : ' + str(test_list))
res = [ele[0] for sub in enumerate(test_list) for ele in enumerate(sub[1])]
res = res[K]
print('Index of character at Kth position word : ' + str(res))