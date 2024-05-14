import collections
even_nums = (2, 4, 6, 8, 10)
even_deque = collections.deque(even_nums)
print('Even numbers:')
print(even_deque)
even_deque.extend(more_even_nums)
print('More even numbers:')
print(even_deque)