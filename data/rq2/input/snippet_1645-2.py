test_str = 'GeeksforGeeks'
print('The original string is : ' + test_str)
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
res = max(all_freq, key=all_freq.get)
print('The maximum of all characters in GeeksforGeeks is : ' + str(res))