#Source: https://stackoverflow.com/questions/65094355/getting-nameerror-even-though-variable-is-defined
a = [2, 4]
b = [16, 32, 96]
maxOfb = max(b)
factorOfb = []
for i in range(1, int(maxOfb/2)):
    if all(j % i == 0 for j in b):
        factorOfb.append(j)
print(factorOfb)