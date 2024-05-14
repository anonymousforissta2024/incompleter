nums = [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
print('Original list:', nums)
print('Minimum value: ', min(numbers))
print('Maximum value: ', max(numbers))
numbers = list(set(numbers))
numbers = sorted(map(lambda n: n * 5, numbers))
print('Result:')
for numb in numbers:
    print(numb, end=' ')