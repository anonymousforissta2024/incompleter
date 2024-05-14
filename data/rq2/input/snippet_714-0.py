def unique_product(list_data):
    temp = list(set(list_data))
    p = 1
    for i in temp:
        p *= i
    return p
print('Original List : ', nums)
print('Product of the unique numbers of the said list: ', unique_product(nums))