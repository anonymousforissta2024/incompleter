import re
print('The original string is : ' + str(test_str))
que_word = 'geek'
temp = []
for sub in re.findall(que_word + '.', test_str):
    temp.append(sub[-1])
res = {que_word: temp.count(que_word) for que_word in temp}
print('The Characters Frequency is : ' + str(res))