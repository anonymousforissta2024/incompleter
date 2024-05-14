def remove_words(in_list, char_list):
    new_list = []
    for line in in_list:
        new_words = ' '.join([word for word in line.split() if not any([phrase in word for phrase in char_list])])
        new_list.append(new_words)
    return new_list
str_list = ['Red color', 'Orange#', 'Green', 'Orange @', 'White']
print('Original list:')
print('list1:', str_list)
print('\nCharacter list:')
print(char_list)
print('\nNew list:')
print(remove_words(str_list, char_list))