str = input('Enter the String:')
for i in range(len(str)):
    if str[i] == ' ':
        continue
    num = ord(str[i])
    arr[num] += 1
print('Frequency of character in a string are:')
for i in range(256):
    if arr[i] != 0:
        print(chr(i), ' occurs ', arr[i], ' times')