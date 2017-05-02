"""An abstract for Widget class"""
import abc


class Widget(metaclass=abc.ABCMeta):
    """Widget abstract"""
    def __init__(self, coords):
        self.coords = coords

    @abc.abstractmethod
    def draw_widget(self, lcd):
        """draw a tile"""
        pass

    @abc.abstractmethod
    def draw_values(self, lcd, force=False):
        """draw a changed values. With force must redraw all values"""
        pass

    @abc.abstractmethod
    def change_values(self, values):
        """change a value, values is a dict [name] = value"""
        pass

    def draw_number(self, lcd, pos_x, pos_y, font, current, previous, spacing=30):
        """draw a number"""
        lcd.transparency_color = font.get_transparency()
        for idx in range(0, len(current)):
            if previous is None or current[idx] != previous[idx]:
                lcd.draw_image(
                    pos_x + (idx * spacing),
                    pos_y,
                    font.get(int(current[idx]))
                )
