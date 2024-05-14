str = input('Enter the String:')
str2 = []
i = 0
while i < len(str):
    ch = str[i]
    if not ch.isupper():
        str2.append(ch)
    i += 1
print('After removing uppercase letter string is:', Final_String)