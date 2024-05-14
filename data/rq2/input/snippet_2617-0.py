str = input('Enter the String:')
for i in range(len(str)):
    if str[i] == ' ':
        continue
    num = ord(str[i])
    arr[num] += 1
print('Repeated character in a string are:')
for i in range(256):
    if arr[i] > 1:
        print(chr(i), ' occurs ', arr[i], ' times')