#Source: https://stackoverflow.com/questions/32312371/typeerror-int-object-is-not-iterable
import random
l = []
for i in range(0,8):
        key = random.randrange(33,126)
        key = chr(key)
        l.append(key)
print(" ".join(l))
x = (round(sum([ord(c) for c in l]) / 8) - 32)
print(x)
if l[i]:
        [ord(c) for c in x]