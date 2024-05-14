from operator import itemgetter

def spermutations(n):
    """permutations by swapping. Yields: perm, sign"""
    sign = 1
    p = [[i, 0 if i == 0 else -1] for i in range(n)]
    if DEBUG:
        print(' #', p)
    yield (tuple((pp[0] for pp in p)), sign)
    while any((pp[1] for pp in p)):
        i1, (n1, d1) = max(((i, pp) for i, pp in enumerate(p) if pp[1]), key=itemgetter(1))
        sign *= -1
        if d1 == -1:
            i2 = i1 - 1
            p[i1], p[i2] = (p[i2], p[i1])
            if i2 == 0 or p[i2 - 1][0] > n1:
                p[i2][1] = 0
        elif d1 == 1:
            i2 = i1 + 1
            p[i1], p[i2] = (p[i2], p[i1])
            if i2 == n - 1 or p[i2 + 1][0] > n1:
                p[i2][1] = 0
        if DEBUG:
            print(' #', p)
        yield (tuple((pp[0] for pp in p)), sign)
        for i3, pp in enumerate(p):
            n3, d3 = pp
            if n3 > n1:
                pp[1] = 1 if i3 < i2 else -1
                if DEBUG:
                    print(' # Set Moving')
if __name__ == '__main__':
    from itertools import permutations
    for n in (3, 4):
        print('\nPermutations and sign of %i items' % n)
        sp = set()
        for i in spermutations(n):
            sp.add(i[0])
            print('Permutation: %r Sign: %2i' % i)
        p = set(permutations(range(n)))
        assert sp == p, 'Two methods of generating permutations do not agree'