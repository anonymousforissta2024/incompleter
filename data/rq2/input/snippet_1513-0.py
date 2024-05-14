print('The original dictionary : ' + str(test_dict))
res = {key: dict(sorted(val.items(), key=lambda ele: ele[1])) for key, val in test_dict.items()}
print('The sorted dictionary : ' + str(res))