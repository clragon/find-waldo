from .Logger import *
import numpy as np
from config import *


class ImageSource:
    image = None
    scale_factor = 0

    def __init__(self):
        Logger.debug("ImageSource initialized")

    def show(self):
        self.image.show()

    def get_width(self):
        return self.image.width

    def get_height(self):
        return self.image.height

    def get_image(self):
        return self.image

    def set_scale_factor(self, picture_width=PICTURE_WIDTH):
        Logger.debug("Setting scale factor for a picture wit width=", picture_width)
        Logger.debug("Scale factor = {}".format(self.image.width/picture_width))
        self.scale_factor = self.image.width/picture_width

    def get_scale_factor(self):
        if self.scale_factor == 0:
            self.set_scale_factor()
        return self.scale_factor

    def get_numpy_array(self):
        (im_width, im_height) = self.image.size
        image_np = np.array(self.image.getdata())
        reshaped = image_np.reshape((im_height, im_width, 3))
        result = reshaped.astype(np.uint8)
        return result
