"""Widget for Node One sensor. Displas data from it in form of tile"""
from view.widget import Widget
from PIL import Image


class NodeOneWidget(Widget):
    """Class NodeOneWidget"""
    def __init__(self, font):
        super().__init__()
        self.font = font
        self.colours = {
            'background': (255, 250, 0),
            'digit_background': (0, 0, 0),
            'border': (244, 244, 244)
        }
        self.current = {
            'temperature': 0,
            'humidity': 0,
            'movement': False,
            'light': False
        }
        self.screen = {
            'temperature': None,
            'humidity': None,
            'movement': None,
            'light': None
        }
        self.icon = {
            'movement': Image.open('assets/image/movement.png'),
            'light': Image.open('assets/image/lightbulb.png'),
            'temperature': Image.open('assets/image/thermometer.png'),
            'humidity': Image.open('assets/image/humidity.png')
        }
        self.initialized = False

    def draw_widget(self, lcd, coords):
        """draw a tile"""
        pos_x, pos_y = coords[0]
        lcd.background_color = self.colours['background']
        lcd.fill_rect(pos_x, pos_y, pos_x + 105, pos_y + 105)

        lcd.background_color = self.colours['digit_background']
        lcd.fill_rect(pos_x+35, pos_y+5, pos_x+57, pos_y+46)
        lcd.fill_rect(pos_x+62, pos_y+5, pos_x+84, pos_y+46)
        lcd.fill_rect(pos_x+35, pos_y+55, pos_x+57, pos_y+95)
        lcd.fill_rect(pos_x+62, pos_y+55, pos_x+84, pos_y+95)

        lcd.transparency_color = (0, 0, 0)
        lcd.draw_image(pos_x + 91, pos_y + 10, self.icon['temperature'])
        lcd.draw_image(pos_x + 88, pos_y + 58, self.icon['humidity'])

        lcd.color = self.colours['border']
        lcd.draw_rect(pos_x, pos_y, pos_x + 105, pos_y + 105)

        self.draw_values(lcd, coords, True)
        self.initialized = True

    def draw_values(self, lcd, coords, force=False):
        """draw values"""
        pos_x, pos_y = coords[0]
        current = {
            'temperature': str(self.current['temperature']).rjust(2, '0'),
            'humidity': str(self.current['humidity']).rjust(2, '0'),
            'movement': self.current['light'],
            'light': self.current['movement']
        }
        screen = {
            'temperature': None if self.screen['temperature'] is None
            else str(self.screen['temperature']).rjust(2, '0'),
            'humidity': None if self.screen['humidity'] is None
            else str(self.screen['humidity']).rjust(2, '0'),
            'movement': self.screen['movement'],
            'light': self.screen['light']

        }
        lcd.transparency_color = self.font.get_transparency()
        if force or current['temperature'] != screen['temperature']:
            self.draw_number(
                lcd, pos_x + 35, pos_y + 5, self.font,
                current['temperature'], screen['temperature'], 27,
                force
            )

        if force or current['humidity'] != screen['humidity']:
            self.draw_number(
                lcd, pos_x + 35, pos_y + 55, self.font,
                current['humidity'], screen['humidity'], 27,
                force
            )

        if force or self.current['light'] != self.screen['light']:
            if self.current['light']:
                lcd.transparency_color = (0, 0, 0)
                lcd.draw_image(pos_x + 7, pos_y + 5, self.icon['light'])
            else:
                lcd.background_color = self.colours['background']
                lcd.fill_rect(pos_x+7, pos_y+5, pos_x+27, pos_y+25)

        if force or self.current['movement'] != self.screen['movement']:
            if self.current['movement']:
                lcd.transparency_color = (0, 0, 0)
                lcd.draw_image(pos_x + 7, pos_y + 30, self.icon['movement'])
            else:
                lcd.background_color = self.colours['background']
                lcd.fill_rect(pos_x+7, pos_y+30, pos_x+27, pos_y+50)

        self.screen = self.current.copy()

    def change_values(self, values):
        """change values"""
        if not self.initialized:
            return
        if 'temp' in values:
            self.current['temperature'] = values['temp']

        if 'humi' in values:
            self.current['humidity'] = values['humi']

        if 'pir' in values:
            self.current['movement'] = values['pir']

        if 'light' in values:
            self.current['light'] = values['light']
