def number_of_substrings(str):
    str_len = len(str)
    return int(str_len * (str_len + 1) / 2)
print('Number of substrings:')
print(number_of_substrings(str1))