def square_num(n):
    return n * n
print('Original List: ', nums)
result = map(square_num, nums)
print('Square the elements of the said list using map():')
print(list(result))