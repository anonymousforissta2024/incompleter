from itertools import groupby
print('The original string is : ' + test_str)
res = [len(list(j)) for _, j in groupby(test_str)]
print('The Consecutive characters frequency : ' + str(res))