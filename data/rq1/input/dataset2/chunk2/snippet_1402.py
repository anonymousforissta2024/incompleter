#Source: https://stackoverflow.com/questions/43940194/kivy-typeerror-on-keyboard-down-takes-2-positional-arguments-but-5-were-given
Builder.load_string('''
<PlayerImage>:
    canvas.before:
        PushMatrix
        Rotate:
            angle: self.angle
            axis: (0, 0, 1)
            origin: self.center
    canvas.after:
        PopMatrix
<PlayerImage2>:
    canvas.before:
        PushMatrix
        Rotate:
            angle: self.angle
            axis: (0, 0, 1)
            origin: self.center
    canvas.after:
        PopMatrix
''')