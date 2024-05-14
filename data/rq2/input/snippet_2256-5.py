print('Enter a binary number:')
binary = input()
if len(binary) % 4 == 1:
    binary = '000' + binary
if len(binary) % 4 == 2:
    binary = '00' + binary
if len(binary) % 4 == 3:
    binary = '0' + binary
hex = ''
len = int(len(binary) / 4)
print('len:', len)
i = 0
j = 0
decimal = 0
while i < len:
    st = binary[j:k]
    bin = int(st)
    temp = 0
    remainder = 0
    decimal = 0
    while bin != 0:
        remainder = bin % 10
        bin = bin // 10
        decimal = decimal + remainder * pow(2, temp)
        temp = temp + 1
    if decimal == 15:
        hex = hex + 'F'
    elif decimal == 14:
        hex = hex + 'E'
    elif decimal == 13:
        hex = hex + 'D'
    elif decimal == 12:
        hex = hex + 'C'
    elif decimal == 11:
        hex = hex + 'B'
    elif decimal == 10:
        hex = hex + 'A'
    else:
        hex = hex + str(decimal)
    j = k
    k = k + 4
    i = i + 1
print('Binary to HexaDecimal is ', hex)