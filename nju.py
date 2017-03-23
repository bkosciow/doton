import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)


class Gfx(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pins = {
            'A0': 17,
            'E1': 22,
            'E2': 21,
            'D0': 23,
            'D1': 24,
            'D2': 25,
            'D3': 12,
            'D4': 16,
            'D5': 20,
            'D6': 26,
            'D7': 19
        }

        self.data_pins = [
            'D0', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7'
        ]
        for pin in self.pins:
            GPIO.setup(self.pins[pin], GPIO.OUT)
            GPIO.output(self.pins[pin], 0)

    def init(self):
        """initialize display"""
        GPIO.output(self.pins['A0'], 0)
        GPIO.output(self.pins['E1'], 1)
        GPIO.output(self.pins['E2'], 1)

        init_sequence = [0xae, 0xa4, 0xa9, 0xe2, 0xa0, 0xaf]
        for cmd in init_sequence:
            self.cmd(cmd, 0)
            self.cmd(cmd, 1)

    def cmd(self, char, enable):
        """send command"""
        GPIO.output(self.pins['A0'], 0)
        self.send(char, enable)

    def data(self, char, enable):
        """send data"""
        GPIO.output(self.pins['A0'], 1)
        self.send(char, enable)

    def send(self, data, enable):
        """Write to gpio"""
        GPIO.output(self.pins['E1'], 0)
        GPIO.output(self.pins['E2'], 0)
        for i in self.data_pins:
            value = data & 0x01
            GPIO.output(self.pins[i], value)
            data >>= 1

        GPIO.output(self.pins['E'+str(enable+1)], 1)
        time.sleep(0.00025)
        GPIO.output(self.pins['E1'], 0)
        GPIO.output(self.pins['E2'], 0)

    def set_xy(self, x, y):
        """set xy pos"""
        if x < self.width/2:
            self.cmd(0xB8 | y, 0)
            self.cmd(0x00 | x, 0)
        else:
            self.cmd(0xB8 | y, 1)
            self.cmd(0x00 | (x - self.width//2), 1)

    def draw_pixels(self, x, y, c=0xff):
        """draw a pixel /line"""
        self.set_xy(x, y//8)
        if x < self.width/2:
            self.data(c, 0)
        else:
            self.data(c, 1)

    def fill(self, c=0):
        for j in range(0, self.height//8):
            for i in range(0, self.width):
                self.set_xy(i, j)
                if i < self.width/2:
                    self.data(c, 0)
                else:
                    self.data(c, 1)

g = Gfx(122, 32)
g.init()
g.fill(0)
# g.fill(255)

g.draw_pixels(2, 0, 128)
g.draw_pixels(3, 0, 128)
g.draw_pixels(7, 0, 128)
g.draw_pixels(8, 0, 128)
g.draw_pixels(1, 9, 7)
g.draw_pixels(9, 9, 7)
g.draw_pixels(2, 9, 8)
g.draw_pixels(3, 9, 16)
g.draw_pixels(4, 9, 33)
g.draw_pixels(5, 9, 66)
g.draw_pixels(6, 9, 33)
g.draw_pixels(7, 9, 16)
g.draw_pixels(8, 9, 8)

g.draw_pixels(15, 9, 127)
g.draw_pixels(16, 9, 65)
g.draw_pixels(17, 9, 65)
g.draw_pixels(18, 9, 62)

g.draw_pixels(20, 9, 38)
g.draw_pixels(21, 9, 73)
g.draw_pixels(22, 9, 73)
g.draw_pixels(23, 9, 50)

g.draw_pixels(25, 9, 127)
g.draw_pixels(26, 9, 9)
g.draw_pixels(27, 9, 9)
g.draw_pixels(28, 9, 6)

g.draw_pixels(30, 9, 98)
g.draw_pixels(31, 9, 81)
g.draw_pixels(32, 9, 73)
g.draw_pixels(33, 9, 70)

g.draw_pixels(35, 9, 62)
g.draw_pixels(36, 9, 65)
g.draw_pixels(37, 9, 65)
g.draw_pixels(38, 9, 62)

g.draw_pixels(40, 9, 4)
g.draw_pixels(41, 9, 2+64)
g.draw_pixels(42, 9, 127)
g.draw_pixels(43, 9, 64)

g.draw_pixels(40, 9, 4)
g.draw_pixels(41, 9, 2+64)
g.draw_pixels(42, 9, 127)
g.draw_pixels(43, 9, 64)

g.draw_pixels(45, 9, 97)
g.draw_pixels(46, 9, 25)
g.draw_pixels(47, 9, 5)
g.draw_pixels(48, 9, 3)

# g.fill(0)
# g.draw_pixels(0, 0)
# g.draw_pixels(70, 16, 129)
# g.draw_pixels(120, 2, 153)
