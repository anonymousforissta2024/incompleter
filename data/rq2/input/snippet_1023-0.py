import random

def random_select_nums(n_list, n):
    return random.sample(n_list, n)
print('Original list:')
print(n_list)
selec_nums = 3
result = random_select_nums(n_list, selec_nums)
print('\nSelected 3 random numbers of the above list:')
print(result)