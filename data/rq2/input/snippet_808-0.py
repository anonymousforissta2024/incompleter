def odd_even_transposition(arr: list) -> list:
    arr_size = len(arr)
    for _ in range(arr_size):
        for i in range(_ % 2, arr_size - 1, 2):
            if arr[i + 1] < arr[i]:
                arr[i], arr[i + 1] = (arr[i + 1], arr[i])
    return arr
print('\nOriginal list:')
print(nums)
odd_even_transposition(nums)
print('Sorted order is:', nums)
nums = [5, 9, 10, 3, -4, 5, 178, 92, 46, -18, 0, 7]
print('\nOriginal list:')
print(nums)
odd_even_transposition(nums)
print('Sorted order is:', nums)