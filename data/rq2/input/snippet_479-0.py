def pairwise(l1):
    temp = []
    for i in range(len(l1) - 1):
        current_element, next_element = (l1[i], l1[i + 1])
        x = (current_element, next_element)
        temp.append(x)
    return temp
print('Original lists:')
print(l1)
print('\nIterate over all pairs of consecutive items of the said list:')
print(pairwise(l1))