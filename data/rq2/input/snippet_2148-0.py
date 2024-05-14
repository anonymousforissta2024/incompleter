print('The original tuple : ' + str(test_tuple))
res = tuple(sum(test_tuple, []))
print('The flattened tuple : ' + str(res))