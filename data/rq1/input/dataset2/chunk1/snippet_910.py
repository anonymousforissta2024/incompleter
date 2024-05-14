#Source: https://stackoverflow.com/questions/70097223/adding-image-to-legend-in-matplotlib-returns-error-attributeerror-barcontaine
from matplotlib.transforms import Bbox, TransformedBbox
from matplotlib.legend_handler import HandlerBase
from matplotlib.image import BboxImage

class ImageHandler(HandlerBase):
    def create_artists(self, legend, orig_handle, Xd_, Yd_, W_, H_, fontsize, trans):
        # enlarge the image by these margins
        sx, sy = self.image_stretch 

        # create a bounding box to house the image
        bb = Bbox.from_bounds(Xd_ - sx, Yd_ - sy, W_ + sx, H_ + sy )
        tbb = TransformedBbox(bb, trans)
        image = BboxImage(tbb)
        image.set_data(self.image_data)
        self.update_prop(image, orig_handle, legend)
        return [image]

    def set_image(self, image_path, image_stretch=(0, 0)):
        self.image_data = plt.imread(image_path)
        self.image_stretch = image_stretch
 