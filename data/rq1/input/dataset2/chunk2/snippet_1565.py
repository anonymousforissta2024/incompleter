#Source: https://stackoverflow.com/questions/42044225/typeerror-integer-argument-expected-got-float-in-pil
from PIL import Image

def change_contrast(img, level):
    def truncate(v):
        return 0 if v < 0 else 255 if v > 255 else v


    img = Image.open("C:\\Users\\omar\\Desktop\\Site\\Images\\obama.png")
    img.load()

    factor = (259 * (level+255)) / (255 * (259-level))
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            color = img.getpixel((x, y))
            new_color = tuple(truncate(factor * (c-128) + 128) for c in color)
            img.putpixel((x, y), new_color)

    return img

result = change_contrast('test_image1.jpg', 128)
result.save('test_image1_output.jpg')
print('done')