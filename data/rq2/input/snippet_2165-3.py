import re
uppercase_characters = re.findall('[A-Z]', string)
lowercase_characters = re.findall('[a-z]', string)
numerical_characters = re.findall('[0-9]', string)
special_characters = re.findall('[, .!?]', string)
print('The no. of uppercase characters is', len(uppercase_characters))
print('The no. of lowercase characters is', len(lowercase_characters))
print('The no. of numerical characters is', len(numerical_characters))
print('The no. of special characters is', len(special_characters))