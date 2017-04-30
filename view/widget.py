"""An abstract for Widget class"""
import abc


class Widget(metaclass=abc.ABCMeta):
    """Widget abstract"""
    def __init__(self, pos_x, pos_y, lcd):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.lcd = lcd

    @abc.abstractmethod
    def draw_widget(self):
        """draw a widget"""
        pass

    @abc.abstractmethod
    def draw_values(self, force=False):
        """draw a changed values. With force must redraw all values"""
        pass

    @abc.abstractmethod
    def change_values(self, values):
        """change a value, values is a dict [name] = value"""
        pass