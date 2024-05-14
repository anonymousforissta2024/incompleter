test_str = 'geeksforgeeks is best'
print('The original string is : ' + test_str)
test_list = [2, 4, 7, 10]
temp = list(test_str)
for idx in test_list:
    temp[idx] = repl_char
res = ''.join(temp)
print('The String after performing replace : ' + str(res))