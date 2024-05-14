from collections import Counter
print('Original list:')
print(language)
cnt = Counter(language)
print('\nMost common element of the said list:')
print(cnt.most_common(1)[0][0])