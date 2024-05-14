def unique_list(text_str):
    l = text_str.split()
    temp = []
    for x in l:
        if x not in temp:
            temp.append(x)
    return ' '.join(temp)
print('Original String:')
print(text_str)
print('\nAfter removing duplicate words from the said string:')
print(unique_list(text_str))