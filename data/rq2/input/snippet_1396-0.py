def sort_by_indexes(lst, indexes, reverse=False):
    return [val for _, val in sorted(zip(indexes, lst), key=lambda x: x[0], reverse=reverse)]
l1 = ['eggs', 'bread', 'oranges', 'jam', 'apples', 'milk']
print(sort_by_indexes(l1, l2))
print(sort_by_indexes(l1, l2, True))