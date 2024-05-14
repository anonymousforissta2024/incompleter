str = input('Enter the String:')
i = 0
while i < len(str):
    ch = str[i]
    if not (ch >= '0' and ch <= '9'):
        str2.append(ch)
    i += 1
Final_String = ''.join(str2)
print('After removing numbers string is:', Final_String)