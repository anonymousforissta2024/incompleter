def remove_dictionary(colors, r_id):
    colors[:] = [d for d in colors if d.get('id') != r_id]
    return colors
colors = [{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
print('Original list of dictionary:')
print(colors)
print('\nRemove id', r_id, 'from the said list of dictionary:')
print(remove_dictionary(colors, r_id))