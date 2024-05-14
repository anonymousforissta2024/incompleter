#Source: https://stackoverflow.com/questions/49566391/nameerror-for-importing-random-and-numpy-random-but-nothing-else
rounds = 10
probability = 100
items = [1, 2, 3, 4, 5]
for r in range(1, rounds):
    from numpy.random import uniform
    sample = {item: uniform() < probability for item in items}