#Source: https://stackoverflow.com/questions/43881184/typeerror-init-got-an-unexpected-keyword-argument-no-builder-kivy
root = Builder.load_string('''
Widget:
    Widget:
        PlayerImage:
            source: './rpgArt/person.zip'
            allow_stretch: True
            keep_ratio: True
        PlayerImage2:
            source: './rpgArt/personred.zip'
            allow_stretch: True
            keep_ratio: True
''')