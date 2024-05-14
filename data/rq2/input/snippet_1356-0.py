def moveSpaces(str1):
    no_spaces = [char for char in str1 if char != ' ']
    space = len(str1) - len(no_spaces)
    result = ' ' * space
    return result + ''.join(no_spaces)
print('Original String:\n', s1)
print('\nAfter moving all spaces to the front:')
print(moveSpaces(s1))