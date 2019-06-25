from PIL import Image
import urllib
import os


class Camera:

    def __init__(self, address, port=8080):
        self.address = address
        self.port = port

    def take_photo(self):
        try:
            urllib.request.urlretrieve("http://{}:{}/photoaf.jpg".format(str(self.address), str(self.port)), 'docs/photo/last_photo.jpg')
        except:
            raise Exception("Camera not reachable")
            os.sys.exit()
        
        self.image = Image.open('docs/photo/last_photo.jpg')
        return self.image
