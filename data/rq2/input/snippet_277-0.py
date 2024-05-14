ctr = 0
for n in num:
    if isinstance(n, tuple):
        break
    ctr += 1
print(ctr)