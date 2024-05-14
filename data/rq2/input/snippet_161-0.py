import itertools as it
nums = [[0, 1, 2], [2, 3, 4], [3, 4, 5, 6], [7, 8, 9, 10, 11], [12, 13, 14]]
print('Original list:')
print(nums)

def get_avg(x):
    x = [i for i in x if i is not None]
    return sum(x, 0.0) / len(x)
print('\nAverage of n-th elements in the said list of lists with different lengths:')
print(list(result))