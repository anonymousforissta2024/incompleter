def test(str1):
    result = [int(str1) for str1 in str1.split() if str1.isdigit()]
    return result
print('Original string:', str1)
print('Extract numbers from the said string:')
print(test(str1))