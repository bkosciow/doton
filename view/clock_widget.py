from view.widget import Widget
import datetime


class ClockWidget(Widget):
    """Clock widget"""
    def __init__(self, font):
        super().__init__()
        self.font = font
        self.work = True
        self.current = {
            'hour': datetime.datetime.now().strftime("%H"),
            'minute': datetime.datetime.now().strftime("%M"),
        }
        self.screen = {
            'hour': None,
            'minute': None
        }
        self.colours = {
            'background': (127, 32, 64),
            'digit_background': (0, 0, 0),
            'border': (244, 244, 244)
        }
        self.initialized = False

    def draw_widget(self, lcd, coords):
        """draw a tile"""
        pos_x, pos_y = coords[0]
        lcd.background_color = self.colours['background']
        lcd.fill_rect(pos_x, pos_y, pos_x + 105, pos_y + 105)

        lcd.color = self.colours['border']
        lcd.draw_circle(pos_x+49, pos_y+25, 2)
        lcd.draw_circle(pos_x+49, pos_y+35, 2)

        lcd.color = self.colours['border']
        lcd.draw_rect(pos_x, pos_y, pos_x + 105, pos_y + 105)
        self.draw_values(lcd, coords, True)
        self.initialized = True

    def draw_values(self, lcd, coords, force=False):
        """draw values"""
        pos_x, pos_y = coords[0]
        self.current = {
            'hour': datetime.datetime.now().strftime("%H"),
            'minute': datetime.datetime.now().strftime("%M"),
        }
        self.draw_number(
            lcd, pos_x+7, pos_y+15, self.font,
            self.current['hour'], self.screen['hour'], 20,
            force
        )
        self.draw_number(
            lcd, pos_x+57, pos_y+15, self.font,
            self.current['minute'], self.screen['minute'], 20,
            force
        )
        self.screen = self.current.copy()

    def change_values(self, values):
        pass
