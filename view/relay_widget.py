"""Widget for Relay Node"""
from view.widget import Widget
from view.widget import Clickable
import json
from PIL import Image


class RelayWidget(Widget, Clickable):
    """Class Relay Widget"""
    def __init__(self, message, target_node, socket, address, channels):
        self.colours = {
            'background': (149, 56, 170),
            'border': (244, 244, 244)
        }
        self.message = message
        self.target_node = target_node
        self.channels = channels
        self.current = [0 for _ in range(0, channels)]
        self.previous = [0 for _ in range(0, channels)]
        self.icon = {
            1: Image.open('assets/image/switch_on.png'),
            0: Image.open('assets/image/switch_off.png'),
        }
        self.socket = socket
        self.address = address
        self.initialized = False

    def draw_widget(self, lcd, coords):
        """draw a tile"""
        if len(coords) != self.channels:
            raise Exception('wrong number of channels')

        for pos_x, pos_y in coords:
            lcd.background_color = self.colours['background']
            lcd.fill_rect(pos_x, pos_y, pos_x + 105, pos_y + 105)

            lcd.color = self.colours['border']
            lcd.draw_rect(pos_x, pos_y, pos_x + 105, pos_y + 105)

        self.draw_values(lcd, coords, True)
        self.initialized = True

    def draw_values(self, lcd, coords, force=False):
        """draw values"""
        lcd.transparency_color = (255, 255, 255)
        idx = 0
        for pos_x, pos_y in coords:
            if force or self.current[idx] != self.previous[idx]:
                lcd.draw_image(pos_x + 3, pos_y + 3, self.icon[self.current[idx]])
            idx += 1

    def change_values(self, values):
        """change values"""
        if 'toggle' in values:
            self.previous[values['toggle'][0]] = self.current[values['toggle'][0]]
            self.current[values['toggle'][0]] = values['toggle'][1]

    def action(self, name, index, pos_x, pos_y):
        """toggle a relay"""
        enabled = self.current[index]
        message = self.message.prepare_message({
            'event': 'channel.off' if enabled else 'channel.on',
            'parameters': {
                'channel': index
            },
            'targets': [self.target_node]
        })
        message = json.dumps(message)
        self.socket.sendto(message.encode(), self.address)
        self.change_values({'toggle': [index, enabled ^ 1]})
