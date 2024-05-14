test_str = 'gfg, is, (best, for), geeks'
print('The original string is : ' + test_str)
temp = ''
res = []
for ele in test_str:
    if ele == '(':
        check += 1
    elif ele == ')':
        check -= 1
    if ele == ', ' and check == 0:
        if temp.strip():
            res.append(temp)
        temp = ''
    else:
        temp += ele
if temp.strip():
    res.append(temp)
print('The string after exceptional split : ' + str(res))