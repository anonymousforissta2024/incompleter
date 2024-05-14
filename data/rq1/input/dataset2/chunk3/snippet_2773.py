#Source: https://stackoverflow.com/questions/37191263/how-to-find-integer-representing-code-point-of-special-character-typeerror-ord
characters = ['Č', 'č', 'Š', 'š', 'Ž', 'ž']
codecs = ['iso8859_2', 'cp1250', 'mac_latin2', 'utf-8', 'utf_16_le', 'utf_16_be']

for letter in characters:
    for code in codecs:
        print(letter + ' ' + code + ' ' + str(ord(letter.encode(code))))