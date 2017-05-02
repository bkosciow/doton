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
        """draw a tile"""
        pass

    @abc.abstractmethod
    def draw_values(self, force=False):
        """draw a changed values. With force must redraw all values"""
        pass

    @abc.abstractmethod
    def change_values(self, values):
        """change a value, values is a dict [name] = value"""
        pass

    def draw_number(self, pos_x, pos_y, font, current, previous, spacing=30):
        """draw a number"""
        self.lcd.transparency_color = font.get_transparency()
        for idx in range(0, len(current)):
            if previous is None or current[idx] != previous[idx]:
                self.lcd.draw_image(
                    pos_x + (idx * spacing),
                    pos_y,
                    font.get(int(current[idx]))
                )
