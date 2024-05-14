#Source: https://stackoverflow.com/questions/51088691/typeerror-in-bar-plot-of-matplotlib
def RGB_hist(image):
    colours = ('r','g','b')
    for i, c in enumerate(colours):
        plt.figure(figsize=(20, 4))
        histr = cv2.calcHist([image], [i], None, [256], [0, 256])

        if c == 'r': colours = [((i/256, 0, 0)) for i in range(0, 256)]
        if c == 'g': colours = [((0, i/256, 0)) for i in range(0, 256)]
        if c == 'b': colours = [((0, 0, i/256)) for i in range(0, 256)]


        plt.bar(range(0, 256), histr, color=colours, edgecolor=colours, width=1)

        plt.show()

RGB_hist(image)