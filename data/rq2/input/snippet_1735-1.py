print('The original string : ' + str(test_string))
res = ''.join(sorted(test_string, reverse=True))
print('String after reverse sorting : ' + str(res))