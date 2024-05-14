#Source: https://stackoverflow.com/questions/60700244/example-code-on-kivy-document-keeps-giving-out-typeerror
texture = Texture.create(size=(64, 64))

size = 64 * 64 * 3
buf = [int(x * 255 / size) for x in range(size)]

buf = b''.join(map(chr, buf))    # This is the code with a problem

texture.blit_buffer(buf, colorfmt='rgb', bufferfmt='ubyte')
with self.canvas:
    Rectangle(texture=texture, pos=self.pos, size=(64, 64))