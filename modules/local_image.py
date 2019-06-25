from image_source import image_source
from logger import logger
from PIL import Image


class LocalImage(ImageSource):
    image = None

    def __init__(self, path="docs/imgs/1.jpg"):
        Logger.debug("Loading image at", path)
        self.image = Image.open(path)

    def load(self, num):
        image_path="docs/imgs/" + str(num) + ".jpg"
        Logger.info("Loading image at", image_path)
        self.image = Image.open(image_path)

