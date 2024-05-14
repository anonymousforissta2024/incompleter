str = input('Enter the String:')
j = len(str) - 1
for i in range(len(str)):
    if str[i] == str[j]:
        count += 1
    j -= 1
if count == len(str):
    print('Input string is palindrome')
else:
    print('Input string is not palindrome')