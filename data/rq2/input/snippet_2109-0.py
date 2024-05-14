def pattern(n):
    for i in n:
        print('|', end='')
        print('*' * int(i))
pattern(n)