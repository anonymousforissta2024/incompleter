import re
test_str = 'geeksforgeeks is best for geeks. A geek should take interest.'
print('The original string is : ' + str(test_str))
que_word = 'geek'
temp = []
for sub in re.findall(que_word + '.', test_str):
    temp.append(sub[-1])
print('The Characters Frequency is : ' + str(res))