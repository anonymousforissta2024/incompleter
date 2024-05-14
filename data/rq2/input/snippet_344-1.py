import random
import string
print('Generate a random alphabetical character:')
print(random.choice(string.ascii_letters))
print('\nGenerate a random alphabetical string:')
str1 = ''
for i in range(random.randint(1, max_length)):
    str1 += random.choice(string.ascii_letters)
print(str1)
print('\nGenerate a random alphabetical string of a fixed length:')
str1 = ''
for i in range(10):
    str1 += random.choice(string.ascii_letters)
print(str1)