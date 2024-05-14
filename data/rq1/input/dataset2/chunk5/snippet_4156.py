#Source: https://stackoverflow.com/questions/40901405/yielding-a-typeerror-input-expected-at-most-1-arguments-got-4-this-error-was
def randomLetters():
    numbers = [random.randint(0, 25), random.randint(0, 25)]
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letters = [alphabet[numbers[0]], alphabet[numbers[1]]]
    return letters

letters = randomLetters()
print(letters)
print(letters[0])
user_input = input('Enter a word that begins with', "'" + letters[0] + "'", 'and ends with', "'" + letters[1] + "': ")
new_user_input = user_input.lower()

while (new_user_input[0] != letters[0]) and (new_user_input[len(new_user_input) - 1] != letters[1]):
    print('Invalid input. Try again.')
    new_user_input = input('Enter a word that begins with', "'" + letters[0] + "'", 'and ends with', "'" + letters[1] + "': ")