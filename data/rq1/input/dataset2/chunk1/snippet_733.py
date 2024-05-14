#Source: https://stackoverflow.com/questions/70097223/adding-image-to-legend-in-matplotlib-returns-error-attributeerror-barcontaine
emoji_dataset = os.path.join( os.environ['HOME'], 'Datasets', 'Emojis')
h1 = ImageHandler()
h2 = ImageHandler()

h1.set_image(os.path.join(emoji_dataset, 'man.png'), image_stretch=(0, 20))
h2.set_image(os.path.join(emoji_dataset, 'woman.png'), image_stretch=(0, 20))

ax.legend(  handler_map={rects1: h1, rects2: h2}, 
                        handlelength=2, labelspacing=0.0, 
                        fontsize=36, borderpad=0.15, loc='best', 
                        handletextpad=0.2, borderaxespad=0.15)