def remove_words(list1, remove_words):
    for word in list(list1):
        if word in remove_words:
            list1.remove(word)
    return list1
remove_colors = ['white', 'orange']
print('Original list:')
print(colors)
print('\nRemove words:')
print(remove_colors)
print('\nAfter removing the specified words from the said list:')
print(remove_words(colors, remove_colors))