class screen:
    @property
    def width(self):
        return self._width


    @width.setter
    def width(self, width):
        self._width = width


    @property
    def height(self):
        return self._height


    @height.setter
    def height(self, h):
        self._height = h


    @property
    def resolution(self):
        return self._width * self._height

s = screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
