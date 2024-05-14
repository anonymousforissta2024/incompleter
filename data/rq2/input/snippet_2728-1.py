str = input('Enter the String:')
for i in range(len(str)):
    if str[i] >= 'A' and str[i] <= 'Z':
        ch = str[i]
        break
    else:
        continue
print('First capital letter in a given String is: ', ch)