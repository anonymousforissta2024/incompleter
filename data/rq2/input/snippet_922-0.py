def test(lst):
    previous_digit = 0
    ctr = 0
    for digit in lst:
        if previous_digit == 0 and digit != 0:
            ctr += 1
        previous_digit = digit
    return ctr
print('\nOriginal list:')
print(nums)
print('\nNumber of groups of non-zero numbers separated by zeros of the said list:')
print(test(nums))