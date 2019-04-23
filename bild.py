

class Image(object):
    def __init__(self, data=None, height_in_mm=None, width_in_mm=None):
        self._data = data
        self._height_in_mm = height_in_mm
        self._width_in_mm = width_in_mm

    def __str__(self):
        return "Image height={}mm, width={}mm".format(self.height_in_mm, self._width_in_mm)

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    @data.deleter
    def data(self):
        del self._data

    @property
    def height_in_mm(self):
        return self._height_in_mm

    @height_in_mm.setter
    def height_in_mm(self, value):
        print("height setter")
        self._height_in_mm = value

    @property
    def width_in_mm(self):
        return self._width_in_mm

    @height_in_mm.setter
    def width_in_mm(self, value):
        self._width_in_mm = value


if __name__ == '__main__':
    b = Image(height_in_mm=11)
    b.height_in_mm = 3
    b.width_in_mm = 2
    print(b)

