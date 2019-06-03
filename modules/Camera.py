#!/usr/bin/env python3
from PIL import Image
from .Logger import *
from .ImageSource import ImageSource
import urllib


class Camera(ImageSource):
    image = None
    address = ''
    port = 8080

    def __init__(self, address, port=8080):
        Logger.debug("Setting up camera at", address)
        self.address = address
        self.port = port

    def take_photo(self):
        # Use urllib to get the image from the IP camera
        urllib.request.urlretrieve("http://" + str(self.address) + ":" + str(self.port) + "/photoaf.jpg", 'docs/photo/last_photo.jpg')
        self.image = Image.open('docs/photo/last_photo.jpg')

    def take_selfie(self):
        urllib.request.urlretrieve("http://" + str(self.address) + ":" + str(self.port) + "/photoaf.jpg", 'docs/photo/last_selfie.jpg')
        self.image = Image.open('docs/photo/last_selfie.jpg')