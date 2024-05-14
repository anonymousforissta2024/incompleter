#Source: https://stackoverflow.com/questions/77016551/why-attribute-error-module-pil-has-no-attribute-image-raises-unlike-its-inst
with PIL.Image.open("before1.jpg") as Im:
    Im.show()