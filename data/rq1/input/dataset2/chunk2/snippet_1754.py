#Source: https://stackoverflow.com/questions/55066562/getting-error-typeerror-nonetype-object-is-not-iterable
def user_test():
    '''
    :return: hold user input
    '''
    global user_string
    global user_character
    user_string = print(input("What is the string you would like to use:"))
    user_character = print(input("What is the character you would like to use:"))
    character_count(user_string, user_character)
    reverse(user_string)
    return user_string, user_character;

def reverse(user_string):
    '''
    :param: string
    :return: reverses a string
    '''
    string = user_string
    print (list(reversed(string)))
    return string

def character_count(user_string, user_character):
    '''
    :return: counts the number of occurances of a character in a string
    '''
    string = user_string
    toCount = user_character
    counter = 0

    for letter in string:
            if( letter == toCount):
                    counter += 1
    print(counter)

def main():
    user_test()


main()