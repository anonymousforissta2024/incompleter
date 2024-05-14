print('The original string is : ' + str(test_str))
test_dict = {'geeks': 1, 'best': 6}
for key in test_dict:
    if key in test_str.split(' '):
        test_str = test_str.replace(key, '')
print('The string after replace : ' + str(test_str))