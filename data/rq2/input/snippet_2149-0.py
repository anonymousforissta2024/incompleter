print('The original list is : ' + str(test_list))
res = len(list(set((tuple(sorted(sub)) for sub in test_list))))
print('Unique tuples Frequency : ' + str(res))