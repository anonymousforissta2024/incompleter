spl_word = 'best'
print('The original string : ' + str(test_string))
print('The split string : ' + str(spl_word))
res = test_string.partition(spl_word)[0]
print('String before the substring occurrence : ' + res)