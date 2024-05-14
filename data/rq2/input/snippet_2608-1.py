str = input('Enter the 1st String:')
count = 0
if len(str) != len(str2):
    print('Strings are not the same.')
else:
    for i in range(0, len(str)):
        if str[i] == str2[i]:
            count = 1
            break
    if count != 1:
        print('Input strings are not the same.')
    else:
        print('Input strings are the same.')