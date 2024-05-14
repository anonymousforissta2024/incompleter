import sys
import math as mt
t = 1
for ___ in range(t):
    s = 'abcd'
    l = []
    d = {}
    for i in range(len(s)):
        suma = 0
        pre = 0
        D = 256
        for j in range(i, len(s)):
            pre = (pre * D + ord(s[j])) % mod
            if d.get(pre, -1) == -1:
                l.append([i, j])
            d[pre] = 1
    print(len(l))
    for i in range(len(l)):
        print(s[l[i][0]:l[i][1] + 1], end=' ')