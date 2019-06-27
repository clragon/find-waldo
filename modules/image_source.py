import numpy as np
from config import *
from PIL import Image, ImageDraw


class ImageSource:
    image = None
    scale_factor = 0

    def show(self):
        self.image.show()

    def get_image(self):
        return self.image

    def set_scale_factor(self, picture_width=PICTURE_WIDTH):
        self.scale_factor = self.image.width/picture_width

    def get_scale_factor(self):
        if self.scale_factor == 0:
            self.set_scale_factor()
        return self.scale_factor

    def mark(self, box):
        # img = Image.open("../docs/imgs/ti8m-group.jpg").convert("RGB")
        empty = Image.new('RGBA', self.image.size, (255,255,255,0))
        base = Image.open(self.image.filename).convert("RGBA")
        result = ImageDraw.Draw(empty)
        result.rectangle(box, outline="red")
        out = Image.alpha_composite(base, empty)
        out.save("heads/aws_out.png")

    def crop(self, box):
        if box is None:
            box = self.box
        self.image.crop(box)

    def save(self, path):
        self.image.save(path)

    def get_path(self):
        return self.image.filename

    def get_size(self):
        return self.image.size
