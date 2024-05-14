#Source: https://stackoverflow.com/questions/55673906/typeerror-str-object-is-not-callable-when-extracting-from-list
game = [['Stack 6', 'Suit D', 9, 6],
  ['Stack 4', 'Suit B', 5, 0]]

for instructions in game:
    for placement in instructions:
        if 'Stack 6' in placement():
            print(placement)