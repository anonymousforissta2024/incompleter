import itertools
for combo in itertools.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))