from collections import Counter
str = 'abcd'
print('Orginal list of strings:')
print(texts)
result = list(filter(lambda x: Counter(str) == Counter(x), texts))
print("\nAnagrams of 'abcd' in the above string: ")
print(result)