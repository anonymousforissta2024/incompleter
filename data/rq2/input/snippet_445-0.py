import collections
odd_deque = collections.deque(odd_nums)
print('Original Deque object with odd numbers:')
print(odd_deque)
print('Deque length: %d' % len(odd_deque))
odd_deque.clear()
print('Deque object after removing all numbers-')
print(odd_deque)
print('Deque length:%d' % len(odd_deque))