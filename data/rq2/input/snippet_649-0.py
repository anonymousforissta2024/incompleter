print('Orginal list of strings:')
print(texts)
result = list(filter(lambda x: x == ''.join(reversed(x)), texts))
print('\nList of palindromes:')
print(result)