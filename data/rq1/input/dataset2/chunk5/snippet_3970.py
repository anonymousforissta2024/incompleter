#Source: https://stackoverflow.com/questions/59116366/typeerror-int-object-is-not-subscriptable-error
from PIL import Image, ImageDraw
from numpy import asarray
# Load image:
input_image = Image.open("Cameraman.tif")
input_pixels = input_image.load()

# Box Blur kernel
box_kernel = ([[-1, -1, -1],
                   [-1, 8, -1],
                   [-1, -1, -1]])


# Select kernel here:
kernel = box_kernel

# Middle of the kernel
offset = len(kernel) // 2

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Compute convolution between intensity and kernels
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Compute convolution with kernel
for x in range(offset, input_image.width - offset):
    for y in range(offset, input_image.height - offset):
        acc = [0, 0, 0]
        for a in range(len(kernel)):
            for b in range(len(kernel)):
                xn = x + a - offset
                yn = y + b - offset
                pixel = input_pixels[xn, yn]
                acc[0] = acc[0] + (pixel[0] * kernel[a][b])
                acc[1] = acc[1] + (pixel[1] * kernel[a][b])
                acc[2] = acc[2] + (pixel[2] * kernel[a][b])

        draw.point((x, y), (int(acc[0]), int(acc[1]), int(acc[2])))

output_image.save("Filtered.png")

img1arr = asarray(input_image)
img2arr = asarray(output_image)
im1arrF = img1arr.astype('float')
im2arrF = img2arr.astype('float')
additionF = (im1arrF+im2arrF)/2
addition = additionF.astype('uint8')
resultImage = Image.fromarray(addition)
resultImage.save('Sharpened.jpg')