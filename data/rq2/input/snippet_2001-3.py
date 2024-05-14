test_str = 'geeksforgeeks'
print('The original string is : ' + test_str)
r_rot = 7
res = (test_str * 3)[len(test_str) + r_rot - l_rot:2 * len(test_str) + r_rot - l_rot]
print('The string after rotation is : ' + str(res))