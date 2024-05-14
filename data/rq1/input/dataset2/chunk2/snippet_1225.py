#Source: https://stackoverflow.com/questions/31771559/finding-most-frequent-number-in-a-list-typeerror-unhashable-type-list
from collections import Counter
def opportunity(a,h):
   ar = []
   ar.append( [row[h] for row in a if len(row)>h] )
   b = Counter(ar)
   return b.most_common(1)

next = opportunity(take, head)