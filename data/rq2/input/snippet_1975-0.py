def countX(lst, x):
    count = 0
    for ele in lst:
        if ele == x:
            count = count + 1
    return count
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))