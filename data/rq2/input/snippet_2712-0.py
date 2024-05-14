str = input('Enter the 1st String:')
if len(str) != len(str2):
    print('Strings are not an Anagrams.')
else:
    count = 0
    str3 = ''.join(sorted(str))
    str4 = ''.join(sorted(str2))
    for i in range(len(str)):
        if str3[i] != str4[i]:
            count = 1
    if count == 1:
        print('Input strings are not an anagram')
    else:
        print('Input strings are an anagram')