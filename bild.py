

class Image(object):
    def __init__(self, data=None, width_in_mm=None, height_in_mm=None):
        """
        Encapsulates image taken by the roboter.
        :param data: actual image content (i.e. pixel values)
        :param width_in_mm: width of the image in pixels
        :param height_in_mm: height of the image in pixels
        """
        self.data = data
        self.height_in_mm = height_in_mm
        self.width_in_mm = width_in_mm

    def __str__(self):
        return "Image width={}mm, height={}mm".format(self.width_in_mm, self.height_in_mm)

    def get_size_in_mm(self):
        return self.width_in_mm, self.height_in_mm

    def get_pixel_values(self):
        """
        TODO: should return a 3 dimensional array of size [height, width, channels] containing the pixels values
        :return:
        """
        return self.data


if __name__ == '__main__':
    b = Image(height_in_mm=11)
    b.height_in_mm = 3
    b.width_in_mm = 2
    print(b)

