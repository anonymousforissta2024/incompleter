#Source: https://stackoverflow.com/questions/46630857/filenotfounderror-on-python
img = printscreen_pil
img = img.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(2)
img = img.convert('1')
img.save('temp.jpg')
text = pytesseract.image_to_string(Image.open('temp.jpg'))