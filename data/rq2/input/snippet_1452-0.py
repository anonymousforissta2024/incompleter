from heapq import nlargest
from operator import itemgetter
for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name, value)