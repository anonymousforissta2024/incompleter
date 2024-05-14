test_str = 'geeksforgeeks is best'
print('The original string is : ' + test_str)
repl_char = '*'
temp = list(test_str)
for idx in test_list:
    temp[idx] = repl_char
res = ''.join(temp)
print('The String after performing replace : ' + str(res))