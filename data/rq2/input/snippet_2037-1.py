print('The original dictionary : ' + str(test_dict))
res = dict()
for key, val in test_dict.items():
    for key_in, val_in in val.items():
        if key_in not in res:
            temp = dict()
        else:
            temp = res[key_in]
        temp[key] = val_in
        res[key_in] = temp
print('The rearranged dictionary : ' + str(res))