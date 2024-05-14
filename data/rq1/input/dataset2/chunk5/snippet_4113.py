#Source: https://stackoverflow.com/questions/44220270/typeerror-shown-even-though-indices-given-are-of-integer-value
for i in range(length - k + 1):
     temp = int(s[i, i + k])   #Error occuring here
     sum_l = 0      