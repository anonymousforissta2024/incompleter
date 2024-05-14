s = input('Input a string')
for c in s:
    if c.isdigit():
        d = d + 1
    elif c.isalpha():
        l = l + 1
    else:
        pass
print('Letters', l)
print('Digits', d)