test_str = 'geeksforgeeks is best for geeks'
print('The original string is : ' + str(test_str))
res = test_str[:test_str.index(sub_str) + len(sub_str)]
print('The string after removal : ' + str(res))