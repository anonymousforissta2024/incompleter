test_dict = {'Gfg': [6, 7, 4], 'is': [4, 3, 2], 'best': [7, 6, 5]}
print('The original dictionary is : ' + str(test_dict))
temp1 = {val: sum((int(idx) for idx in key)) for val, key in test_dict.items()}
temp2 = sorted(temp1.items(), key=lambda ele: temp1[ele[0]])
print('The sorted dictionary : ' + str(res))