def count_range_in_list(li, min, max):
    ctr = 0
    for x in li:
        if min <= x <= max:
            ctr += 1
    return ctr
print(count_range_in_list(list1, 40, 100))
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(count_range_in_list(list2, 'a', 'e'))