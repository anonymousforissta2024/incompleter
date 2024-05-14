def test(lst):
    result = []
    ele_val = 0
    for digit in lst:
        if digit == 0:
            if ele_val != 0:
                result.append(ele_val)
                ele_val = 0
        else:
            ele_val += digit
    if ele_val > 0:
        result.append(ele_val)
    return result
print('\nOriginal list:')
print(nums)
print('\nCompute the sum of non-zero groups (separated by zeros) of the said list of numbers:')
print(test(nums))