#!/usr/bin/env python3

import requests
import numpy as np
from PIL import Image as PilImage

from .image import Image
from cam_config import REAL_IMAGE_WIDTH_IN_MM, REAL_IMAGE_HEIGHT_IN_MM


class Camera():
    def take_snapshot(self, url):   
        print ("take_snapshot")
        # Use urllib to get the image from the IP camera
        urllib.request.urlretrieve(url, 'last_photo.jpg')
        img = np.array(PilImage.open('docs/last_photo.jpg').rotate(270, expand=True))

        return Image(data=img, width_in_mm=REAL_IMAGE_WIDTH_IN_MM, height_in_mm=REAL_IMAGE_HEIGHT_IN_MM)

    def __init__(self):
        print ("__init__")
