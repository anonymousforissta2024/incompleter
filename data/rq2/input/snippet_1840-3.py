test_str = 'Geeksforgeeks is best for geeks and CS'
print('The original string is : ' + str(test_str))
word_list = ['best', 'CS', 'for']
res = ' '.join([repl_wrd if idx in word_list else idx for idx in test_str.split()])
print('String after multiple replace : ' + str(res))