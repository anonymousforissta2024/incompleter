#Source: https://stackoverflow.com/questions/75659289/getting-typeerror-jpegimagefile-object-is-not-callable-while-asking-for-user
from PIL import Image

input_path = 'seal.jpeg'
output_path = 'output.png'

# Open the input image
input_image = Image.open(input_path)

if input_image.mode == 'RGBA':
    # If the image is already transparent, do nothing
    print("Image is already transparent")
else:
    # Convert to RGBA mode to have alpha channel
    rgba = input_image.convert('RGBA')

    # Create a new transparent image with same size
    output_image = Image.new('RGBA', rgba.size, (0,0,0,0))

    # Loop through all the pixels
    for x in range(rgba.size[0]):
        for y in range(rgba.size[1]):
            # Get the RGBA values of the pixel
            r,g,b,a = rgba.getpixel((x,y))
            # Check if the pixel is not too bright (not white or near white)
            if sum((r,g,b)) < 600:
                # Set the pixel in the output image with the same color and alpha value
                output_image.putpixel((x,y), (r,g,b,a))

    # Ask user if they want to resize the output image
    resize_str = "Output image is {}x{} pixels. Do you want to resize it? (y/n): ".format(output_image.size[0], output_image.size[1])
    resize_choice = input("{}".format(resize_str))
    if resize_choice.lower() == "y":
        percent_str = "Enter desired resize percentage (e.g. 50 for 50%): "
        resize_percent = int(input("{}".format(percent_str)))
        resize = (int(output_image.size[0]*resize_percent/100), int(output_image.size[1]*resize_percent/100))
        output_image = output_image.resize(resize)

    # Save the output image
    output_image.save(output_path)