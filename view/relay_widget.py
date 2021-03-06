"""Widget for Relay Node"""
from view.widget import Widget
from view.widget import Clickable
import json
from PIL import Image
from iot_message.message import Message
# from iot_message.factory import MessageFactory


class RelayWidget(Widget, Clickable):
    """Class Relay Widget"""
    def __init__(self, target_node, socket, address, channels):
        super().__init__()
        self.colours = {
            'background': (149, 56, 170),
            'border': (244, 244, 244)
        }
        self.target_node = target_node
        self.channels = channels
        self.current = [0 for _ in range(0, channels)]
        self.screen = [0 for _ in range(0, channels)]
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
        current = self.current.copy()
        for pos_x, pos_y in coords:
            if force or current[idx] != self.screen[idx]:
                lcd.draw_image(pos_x + 13, pos_y + 13, self.icon[current[idx]])
            idx += 1
        self.screen = current.copy()

    def change_values(self, values):
        """change values"""
        if 'states' in values:
            for idx in range(len(values['states'])):
                self.current[idx] = values['states'][idx]

    def action(self, name, index, pos_x, pos_y):
        """toggle a relay"""
        enabled = self.current[index]
        message = Message()
        message.set({
            'event': 'channel.off' if enabled else 'channel.on',
            'parameters': {
                'channel': index
            },
            'targets': [self.target_node]
        })
        message.encoder = self.encoder_idx
        print(message)
        self.socket.sendto(bytes(message), self.address)
