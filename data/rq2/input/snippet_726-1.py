from heapq import nlargest
three_largest = nlargest(3, my_dict, key=my_dict.get)
print(three_largest)