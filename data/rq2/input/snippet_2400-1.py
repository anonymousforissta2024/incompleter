str = input('Enter the String:')
v_count = 0
s_count = 0
for i in range(len(str)):
    if str[i] == 'a' or str[i] == 'A' or str[i] == 'e' or (str[i] == 'E') or (str[i] == 'i') or (str[i] == 'I') or (str[i] == 'o') or (str[i] == 'O') or (str[i] == 'u') or (str[i] == 'U'):
        v_count += 1
    elif str[i] >= '0' and str[i] <= '9':
        n_count += 1
    elif str[i] >= chr(0) and str[i] <= chr(47) or (str[i] >= chr(58) and str[i] <= chr(64)) or (str[i] >= chr(91) and str[i] <= chr(96)) or (str[i] >= chr(123) and str[i] <= chr(127)):
        s_count += 1
print('Number of digits: ', n_count)
print('Number of vowels: ', v_count)
print('Number of special character: ', s_count)
print('Number of consonants: ', len(str) - n_count - v_count - s_count)