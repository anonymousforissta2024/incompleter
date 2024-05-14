test_list = ['geekforgeeks', 'is', 'best', 'for', 'geeks']
print('The original list is : ' + str(test_list))
res = sorted(test_list, key=lambda ele: -ele.count(K))
print('Sorted String : ' + str(res))