def test(lst):
    result = sorted(lst, key=lambda x: not x)
    return result
print('\nOriginal list:')
print(nums)
print('\nMove all zero digits to end of the said list of numbers:')
print(test(nums))