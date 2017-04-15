import abc


class Chip(metaclass=abc.ABCMeta):
    def __init__(self, width, height, driver):
        self._width = width
        self._height = height
        self.driver = driver

    @property
    def width(self):
        """get width"""
        return self._width

    @property
    def height(self):
        """get height"""
        return self._height

    @abc.abstractmethod
    def init(self):
        """init a chipset"""
        pass

    @abc.abstractmethod
    def draw_pixel(self, x, y):
        """draw a pixel at x,y"""
        pass

    @abc.abstractmethod
    def draw_line(self, x1, y1, x2, y2):
        """draw a line from point x1,y1 to x2,y2"""
        pass

    @abc.abstractmethod
    def draw_rect(self, x1, y1, x2, y2):
        """draw a rectangle"""
        pass

    @abc.abstractmethod
    def draw_circle(self, x, y, r):
        """draw a circle"""
        pass

    @abc.abstractmethod
    def draw_arc(self, x, y, radius, start, end):
        """draw an arc"""
        pass

    @abc.abstractmethod
    def fill_rect(self, x1, y1, x2, y2):
        """draw a filled rectangle"""
        pass
