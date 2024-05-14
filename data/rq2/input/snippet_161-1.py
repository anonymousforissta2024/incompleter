import itertools as it
print('Original list:')
print(nums)

def get_avg(x):
    x = [i for i in x if i is not None]
    return sum(x, 0.0) / len(x)
result = map(get_avg, it.zip_longest(*nums))
print('\nAverage of n-th elements in the said list of lists with different lengths:')
print(list(result))