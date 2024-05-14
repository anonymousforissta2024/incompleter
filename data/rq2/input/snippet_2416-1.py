str = input('Enter the String:')
newStr = ''
for i in range(len(str)):
    if j % 2 == 1:
        if str[i] >= 'A' and str[i] <= 'Z':
            ch = chr(ord(str[i]) + 32)
            newStr = newStr + ch
        else:
            newStr = newStr + str[i]
    elif str[i] >= 'a' and str[i] <= 'z':
        ch = chr(ord(str[i]) - 32)
        newStr = newStr + ch
    else:
        newStr = newStr + str[i]
    if str[i] == ' ':
        continue
    j = j + 1
print('After converting Your String is :', newStr)