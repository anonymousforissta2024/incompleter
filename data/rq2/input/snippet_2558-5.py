import math
hex = input('Enter Hexadecimal Number:')
value = 0
j = len(hex)
j -= 1
for i in range(0, len(hex)):
    if hex[i] >= '0' and hex[i] <= '9':
        value = int(hex[i])
    if hex[i] == 'A' or hex[i] == 'a':
        value = 10
    if hex[i] == 'B' or hex[i] == 'b':
        value = 11
    if hex[i] == 'C' or hex[i] == 'c':
        value = 12
    if hex[i] == 'D' or hex[i] == 'd':
        value = 13
    if hex[i] == 'E' or hex[i] == 'e':
        value = 14
    if hex[i] == 'F' or hex[i] == 'f':
        value = 15
    decimal = decimal + int(value * math.pow(16, j))
    j -= 1
sem = 1
octal = 0
while decimal != 0:
    octal = octal + decimal % 8 * sem
    decimal = decimal // 8
    sem = int(sem * 10)
print('Octal Number is:', octal)