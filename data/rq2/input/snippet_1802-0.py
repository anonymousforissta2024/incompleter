print('The original list : ' + str(test_list))
res = []
for ele in test_list:
    temp = [[]]
    for char in ele:
        if char.isupper():
            temp.append([])
        temp[-1].append(char)
    res.append(' '.join((''.join(ele) for ele in temp)))
print('The space added list of strings : ' + str(res))