import collections
Output = collections.defaultdict(int)
for elem in Input:
    Output[elem[0]] += 1
print(Output)