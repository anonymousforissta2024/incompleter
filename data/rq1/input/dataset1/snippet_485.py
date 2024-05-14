# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
# Importing Image class from PIL module
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from PIL import Image
    _l_(1538959)

except ImportError:
    pass

# Opens a image in RGB mode
im = _c_(1538962, _a_(1538961, _n_(1538960, "Image", lambda: Image), "open"), r"C:\Users\System-Pc\Desktop\ybear.jpg")
_l_(1538963)

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = _a_(1538965, _n_(1538964, "im", lambda: im), "size")
_l_(1538966)

# Setting the points for cropped image
left = 4
_l_(1538967)
top = _n_(1538968, "height", lambda: height) / 5
_l_(1538969)
right = 154
_l_(1538970)
bottom = 3 * _n_(1538971, "height", lambda: height) / 5
_l_(1538972)

# Cropped image of above dimension
# (It will not change original image)
im1 = _c_(1538979, _a_(1538974, _n_(1538973, "im", lambda: im), "crop"), (_n_(1538975, "left", lambda: left), _n_(1538976, "top", lambda: top), _n_(1538977, "right", lambda: right), _n_(1538978, "bottom", lambda: bottom)))
_l_(1538980)
newsize = (300, 300)
_l_(1538981)
im1 = _c_(1538985, _a_(1538983, _n_(1538982, "im1", lambda: im1), "resize"), _n_(1538984, "newsize", lambda: newsize))
_l_(1538986)
# Shows the image in image viewer
_c_(1538989, _a_(1538988, _n_(1538987, "im1", lambda: im1), "show"))
_l_(1538990)

