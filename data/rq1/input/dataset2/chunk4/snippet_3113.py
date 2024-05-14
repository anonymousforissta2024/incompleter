#Source: https://stackoverflow.com/questions/66552353/pillow-attributeerror-photoimage-object-has-no-attribute-photoimage-photo
path = str(pathlib.Path(__file__).parent.absolute()) + '/Chess/Sprites/W_K.png'
norm_img = Image.open(path)
img = norm_img.resize((50,50))
photo = ImageTk.PhotoImage(image=img)
king = self.base.create_image((100,100),image=photo)