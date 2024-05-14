from collections import Counter
result = Counter()
for d in item_list:
    result[d['item']] += d['amount']
print(result)