#Source: https://stackoverflow.com/questions/57595837/attributeerror-module-string-has-no-attribute-capitalize
import string
s = "nishant sharma"
str = " ".join(map(string.capitalize, s.split(' ')))
print(str)