def remove_dictionary(colors, r_id):
    colors[:] = [d for d in colors if d.get('id') != r_id]
    return colors
print('Original list of dictionary:')
print(colors)
r_id = '#FF0000'
print('\nRemove id', r_id, 'from the said list of dictionary:')
print(remove_dictionary(colors, r_id))