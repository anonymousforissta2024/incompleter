#Source: https://stackoverflow.com/questions/51181824/typeerror-int-object-is-not-subscriptable-when-reversing-a-number
max = 10 ** n
length = 0
total = 0
for i in range (max):
    if i == i[::-1]:
        total += 1
        if len(i) == n:
            length += 1