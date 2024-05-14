print('The original tuple is : ' + str(test_tup))
res = tuple((sorted(sub) for sub in test_tup))
print('The tuple after sorting lists : ' + str(res))