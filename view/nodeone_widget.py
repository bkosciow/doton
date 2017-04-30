from PIL import Image


class NodeOneWidget(object):

    def __init__(self, x, y, lcd, font):
        self.x = x
        self.y = y
        self.lcd = lcd
        self.font = font
        self.colours = {
            'background': (255, 250, 0),
            'digit_background': (0, 0, 0)
        }
        self.temperature = {
            'current': 0,
            'previous': 0
        }
        self.humidity = {
            'current': 0,
            'previous': 0
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
            'light': Image.open('assets/image/lightbulb.png')
        }

    def draw_widget(self):
        """draw widget"""
        self.lcd.background_color = self.colours['background']
        self.lcd.fill_rect(self.x, self.y, self.x + 115, self.y + 103)

        self.lcd.background_color = self.colours['digit_background']
        self.lcd.fill_rect(self.x+40, self.y+5, self.x+62, self.y+46)
        self.lcd.fill_rect(self.x+67, self.y+5, self.x+89, self.y+46)

        self.lcd.fill_rect(self.x+40, self.y+55, self.x+60, self.y+95)
        self.lcd.fill_rect(self.x+67, self.y+55, self.x+89, self.y+95)
        self.draw_values(True)

    def draw_values(self, force=False):
        """draw values"""
        old_transparency = self.lcd.transparency_color
        self.lcd.transparency_color = self.font.get_transparency()
        current = str(self.temperature['current']).rjust(2, '0')
        previous = str(self.temperature['previous']).rjust(2, '0')
        if force or current != previous:
            if force or current[0] != previous[0]:
                self.lcd.draw_image(self.x + 40, self.y + 5, self.font.get(int(current[0])))
            if force or current[1] != previous[1]:
                self.lcd.draw_image(self.x + 67, self.y + 5, self.font.get(int(current[1])))

        current = str(self.humidity['current']).rjust(2, '0')
        previous = str(self.humidity['previous']).rjust(2, '0')
        if force or current != previous:
            if force or current[0] != previous[0]:
                self.lcd.draw_image(self.x + 40, self.y + 55, self.font.get(int(current[0])))
            if force or current[1] != previous[1]:
                self.lcd.draw_image(self.x + 67, self.y + 55, self.font.get(int(current[1])))

        if force or self.light['current'] != self.light['previous']:
            if self.light['current']:
                self.lcd.transparency_color = (0, 0, 0)
                self.lcd.draw_image(self.x + 5, self.y + 5, self.icon['light'])
            else:
                self.lcd.background_color = self.colours['background']
                self.lcd.fill_rect(self.x+5, self.y+5, self.x+25, self.y+25)

        if force or self.movement['current'] != self.movement['previous']:
            if self.movement['current']:
                self.lcd.transparency_color = (0, 0, 0)
                self.lcd.draw_image(self.x + 5, self.y + 30, self.icon['movement'])
            else:
                self.lcd.background_color = self.colours['background']
                self.lcd.fill_rect(self.x+5, self.y+30, self.x+25, self.y+50)

        self.lcd.transparency_color = old_transparency

    def change_values(self, values):
        """display values"""
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