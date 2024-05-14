def condition_match(x):
    return x % 2 == 0

def remove_items_con(data, N):
    ctr = 1
    result = []
    for x in data:
        if ctr > N or not condition_match(x):
            result.append(x)
        else:
            ctr = ctr + 1
    return result
nums = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]
print('Original list:')
print(nums)
print('\nRemove first 4 even numbers from the said list:')
print(remove_items_con(nums, N))