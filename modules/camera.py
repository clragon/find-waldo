from PIL import Image
from image_source import ImageSource
import urllib


class Camera(ImageSource):
    image = None
    address = ''
    port = 8080
    status = 1

    def __init__(self, address, port=8080):
        self.address = address
        self.port = port

    def set_offline(self):
        self.status = 0

    def set_online(self):
        self.status = 1

    def is_online(self):
        return self.status == 1

    def take_photo(self):
        # Use urllib to get the image from the IP camera
        if self.is_online():
            urllib.request.urlretrieve("http://" + str(self.address) + ":" + str(self.port) + "/photoaf.jpg", 'docs/photo/last_photo.jpg')
        self.image = Image.open('docs/photo/last_photo.jpg')
        return self.image

    def take_selfie(self):
        if self.is_online():
            urllib.request.urlretrieve("http://" + str(self.address) + ":" + str(self.port) + "/photoaf.jpg", 'docs/photo/last_selfie.jpg')
        self.image = Image.open('docs/photo/last_selfie.jpg')
        return self.image
