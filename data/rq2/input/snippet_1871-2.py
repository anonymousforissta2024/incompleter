test_str = 'abcaaaacbbaa'
print('The original string is : ' + str(test_str))
K = 'a'
cnt = 0
for idx in range(len(test_str)):
    if test_str[idx] == K:
        cnt += 1
    else:
        cnt = 0
    res = max(res, cnt)
print('The Longest Substring Length : ' + str(res))