#!/usr/bin/env python3

import urllib.request
import cv2
import numpy as np
import time

from image import Image
from cam_config import REAL_IMAGE_WIDTH_IN_MM, REAL_IMAGE_HEIGHT_IN_MM

class cam():
    def take_snapshot(self, url):   
        print ("take_snapshot")
        # Use urllib to get the image from the IP camera
        imgResp = urllib.request.urlopen(url)
        
        # Numpy to convert into a array
        imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
        
        # Finally decode the array to OpenCV usable format ;) 
        img = cv2.imdecode(imgNp,-1)

        return Image(data=img, width_in_mm=REAL_IMAGE_WIDTH_IN_MM, height_in_mm=REAL_IMAGE_HEIGHT_IN_MM)

    def __init__(self):
        print ("__init__")
