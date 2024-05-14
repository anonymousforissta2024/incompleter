def remove_words(list1, remove_words):
    for word in list(list1):
        if word in remove_words:
            list1.remove(word)
    return list1
colors = ['red', 'green', 'blue', 'white', 'black', 'orange']
print('Original list:')
print(colors)
print('\nRemove words:')
print(remove_colors)
print('\nAfter removing the specified words from the said list:')
print(remove_words(colors, remove_colors))