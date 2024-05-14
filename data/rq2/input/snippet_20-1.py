def same_order(l1, l2):
    common_elements = set(l1) & set(l2)
    l1 = [e for e in l1 if e in common_elements]
    l2 = [e for e in l2 if e in common_elements]
    return l1 == l2
color1 = ['red', 'green', 'black', 'orange']
color2 = ['red', 'pink', 'green', 'white', 'black']
print('Original lists:')
print(color1)
print(color2)
print(color3)
print('\nTest common elements between color1 and color2 are in same order?')
print(same_order(color1, color2))
print('\nTest common elements between color1 and color3 are in same order?')
print(same_order(color1, color3))
print('\nTest common elements between color2 and color3 are in same order?')
print(same_order(color2, color3))