print('The original dictionary is : ' + str(test_dict))
res = 0
for val in test_dict.values():
    res += val
res = res / len(test_dict)
print('The computed mean : ' + str(res))