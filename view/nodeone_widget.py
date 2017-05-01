"""Widget for Node One sensor. Displas data from it in form of tile"""
from view.widget import Widget
from PIL import Image


class NodeOneWidget(Widget):
    """Class NodeOneWidget"""
    def __init__(self, pos_x, pos_y, lcd, font):
        super().__init__(pos_x, pos_y, lcd)
        self.font = font
        self.colours = {
            'background': (255, 250, 0),
            'digit_background': (0, 0, 0),
            'border': (244, 244, 244)
        }
        self.temperature = {
            'current': 0,
            'previous': None
        }
        self.humidity = {
            'current': 0,
            'previous': None
        }
        self.movement = {
            'current': False,
            'previous': None
        }
        self.light = {
            'current': False,
            'previous': None
        }
        self.icon = {
            'movement': Image.open('assets/image/movement.png'),
            'light': Image.open('assets/image/lightbulb.png'),
            'temperature': Image.open('assets/image/thermometer.png'),
        }

    def draw_widget(self):
        """draw a tile"""
        self.lcd.background_color = self.colours['background']
        self.lcd.fill_rect(self.pos_x, self.pos_y, self.pos_x + 115, self.pos_y + 103)

        self.lcd.background_color = self.colours['digit_background']
        self.lcd.fill_rect(self.pos_x+40, self.pos_y+5, self.pos_x+62, self.pos_y+46)
        self.lcd.fill_rect(self.pos_x+67, self.pos_y+5, self.pos_x+89, self.pos_y+46)

        self.lcd.fill_rect(self.pos_x+40, self.pos_y+55, self.pos_x+60, self.pos_y+95)
        self.lcd.fill_rect(self.pos_x+67, self.pos_y+55, self.pos_x+89, self.pos_y+95)

        self.lcd.transparency_color = (0, 0, 0)
        self.lcd.draw_image(self.pos_x + 95, self.pos_y + 8, self.icon['temperature'])

        self.lcd.color = self.colours['border']
        self.lcd.draw_rect(self.pos_x, self.pos_y, self.pos_x + 115, self.pos_y + 103)

        self.draw_values(True)

    def draw_values(self, force=False):
        """draw values"""
        old_transparency = self.lcd.transparency_color
        self.lcd.transparency_color = self.font.get_transparency()
        current = str(self.temperature['current']).rjust(2, '0')
        previous = None if self.temperature['previous'] is None else str(self.temperature['previous']).rjust(2, '0')
        if force or current != previous:
            self.draw_number(self.pos_x + 40, self.pos_y + 5, self.font, current, previous, 27)

        current = str(self.humidity['current']).rjust(2, '0')
        previous = None if self.humidity['previous'] is None else str(self.humidity['previous']).rjust(2, '0')
        if force or current != previous:
            self.draw_number(self.pos_x + 40, self.pos_y + 55, self.font, current, previous, 27)

        if force or self.light['current'] != self.light['previous']:
            if self.light['current']:
                self.lcd.transparency_color = (0, 0, 0)
                self.lcd.draw_image(self.pos_x + 5, self.pos_y + 5, self.icon['light'])
            else:
                self.lcd.background_color = self.colours['background']
                self.lcd.fill_rect(self.pos_x+5, self.pos_y+5, self.pos_x+25, self.pos_y+25)

        if force or self.movement['current'] != self.movement['previous']:
            if self.movement['current']:
                self.lcd.transparency_color = (0, 0, 0)
                self.lcd.draw_image(self.pos_x + 5, self.pos_y + 30, self.icon['movement'])
            else:
                self.lcd.background_color = self.colours['background']
                self.lcd.fill_rect(self.pos_x+5, self.pos_y+30, self.pos_x+25, self.pos_y+50)

        self.lcd.transparency_color = old_transparency

    def change_values(self, values):
        """change values"""
        if 'temp' in values:
            self.temperature['previous'] = self.temperature['current']
            self.temperature['current'] = values['temp']

        if 'humi' in values:
            self.humidity['previous'] = self.humidity['current']
            self.humidity['current'] = values['humi']

        if 'pir' in values:
            self.movement['previous'] = self.movement['current']
            self.movement['current'] = values['pir']

        if 'light' in values:
            self.light['previous'] = self.light['current']
            self.light['current'] = values['light']
