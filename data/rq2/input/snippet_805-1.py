import collections
even_deque = collections.deque(even_nums)
print('Even numbers:')
print(even_deque)
more_even_nums = (12, 14, 16, 18, 20)
even_deque.extend(more_even_nums)
print('More even numbers:')
print(even_deque)