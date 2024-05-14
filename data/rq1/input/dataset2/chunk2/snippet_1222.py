#Source: https://stackoverflow.com/questions/43940194/kivy-typeerror-on-keyboard-down-takes-2-positional-arguments-but-5-were-given
root = Builder.load_string('''
    Widget:
        Widget:
            PlayerImage:
                source: './rpgArt/person.zip'
                allow_stretch: True
                keep_ratio: True

    ''')