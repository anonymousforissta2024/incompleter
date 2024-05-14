#Source: https://stackoverflow.com/questions/67823362/b-0-lenst-typeerror-object-of-type-function-has-no-len
from turtle import st

mxdiff = 0
buy = 0
sell = 0
a = []  # min array from left
b = [0] * len(st)  # max array from right
d = []  # difference array
minleft = st[0]
maxright = st[len(st) - 1]

for i in range(0, len(st)):
    if (st[i] < minleft):
        minleft = st[i]
        a.append(st[i])
    else:
        a.append(minleft)

for i in range(len(st) - 1, -1, -1):
    if (st[i] > maxright):
        maxright = st[i]
        b[i] = st[i]
    else:
        b[i] = maxright

for i in range(0, len(st)):
    d.append(b[i] - a[i])

mxdiff = max(d)

for i in range(0, len(st)):
    if (d[i] == mxdiff and d[i + 1] == mxdiff):
        buy = i
        break

for i in range(len(st) - 1, -1, -1):
    if (d[i] == mxdiff and d[i - 1] == mxdiff):
        sell = i
        break

print("stocks has to be bought on day ")
print(buy + 1)

print("stocks has to be sold on day ")
print(sell + 1)