print('The original string is : ' + test_str)
punc = '!()-[]{};:\'"\\,<>./?@#$%^&*_~'
for ele in test_str:
    if ele in punc:
        test_str = test_str.replace(ele, '')
print('The string after punctuation filter : ' + test_str)