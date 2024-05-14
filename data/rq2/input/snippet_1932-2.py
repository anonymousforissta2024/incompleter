print('The original dictionary is : ' + str(test_dict))
temp1 = {val: sum((int(idx) for idx in key)) for val, key in test_dict.items()}
temp2 = sorted(temp1.items(), key=lambda ele: temp1[ele[0]])
res = {key: val for key, val in temp2}
print('The sorted dictionary : ' + str(res))