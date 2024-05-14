print('Original list:')
print(color)
print('\nTraverse the said list in reverse order:')
for i in reversed(color):
    print(i)
print('\nTraverse the said list in reverse order with original index:')
for i, el in reversed(list(enumerate(color))):
    print(i, el)