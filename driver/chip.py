import abc


class Chip(metaclass=abc.ABCMeta):
    def __init__(self, width, height, driver, auto_flush):
        self.options = {}
        self._width = width
        self._height = height
        self.driver = driver
        self.options['auto_flush'] = auto_flush

    @property
    def width(self):
        """get width"""
        return self._width

    @property
    def height(self):
        """get height"""
        return self._height

    @abc.abstractmethod
    def _converted_background_color(self):
        """convert RGB background to available color"""
        pass

    @abc.abstractmethod
    def _converted_color(self):
        """convert RGB color to available color"""
        pass

    @property
    def color(self):
        return self.options['color']

    @color.setter
    def color(self, rgb):
        self.options['color'] = {
            'R': rgb[0], 'G': rgb[1], 'B': rgb[2]
        }

    @property
    def background_color(self):
        return self.options['background_color']

    @background_color.setter
    def background_color(self, rgb):
        self.options['background_color'] = {
            'R': rgb[0], 'G': rgb[1], 'B': rgb[2]
        }

    @property
    def auto_flush(self):
        """get auto_flush"""
        return self.options['auto_flush']

    @auto_flush.setter
    def auto_flush(self, value):
        """set auto_flush"""
        self.options['auto_flush'] = bool(value)

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
