print('Original list:', nums)
numbers = list(map(round, nums))
print('Minimum value: ', min(numbers))
print('Maximum value: ', max(numbers))
numbers = list(set(numbers))
numbers = sorted(map(lambda n: n * 5, numbers))
print('Result:')
for numb in numbers:
    print(numb, end=' ')