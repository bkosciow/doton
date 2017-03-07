import RPi.GPIO as GPIO
import time
import itertools


class TFT(object):
    def __init__(self):
        self.pins = {
            'RS': 27,
            'W': 17,
            'DB8': 22,
            'DB9': 23,
            'DB10': 24,
            'DB11': 5,
            'DB12': 12,
            'DB13': 16,
            'DB14': 20,
            'DB15': 21,
            'RST': 25,
        }
        self.data_pins = [
            'DB8', 'DB9', 'DB10', 'DB11', 'DB12', 'DB13', 'DB14', 'DB15',
        ]
        for pin in self.pins:
            GPIO.setup(self.pins[pin], GPIO.OUT)
            GPIO.output(self.pins[pin], 0)

        self.color = {
            'R': 255, 'G': 255, 'B': 255
        }
        self.bcolor = {
            'R': 0, 'G': 0, 'B': 0,
        }

    def cmd(self, cmd):
        """send command to display"""
        GPIO.output(self.pins['RS'], 0)
        self.send(cmd)

    def _set_pins(self, bits):
        """set rpi pins"""
        for pin in self.data_pins:
            value = bits & 0x01
            GPIO.output(self.pins[pin], value)
            bits >>= 1

    def send(self, data):
        """send 16bit as 2*8bit"""
        self._set_pins(data >> 8)
        GPIO.output(self.pins['W'], 0)
        GPIO.output(self.pins['W'], 1)
        self._set_pins(data)
        GPIO.output(self.pins['W'], 0)
        GPIO.output(self.pins['W'], 1)

    def data(self, data):
        """send data to display"""
        GPIO.output(self.pins['RS'], 1)
        self.send(data)

    def cmd_data(self, cmd, data):
        """send command and data"""
        GPIO.output(self.pins['RS'], 0)
        self.send(cmd)
        GPIO.output(self.pins['RS'], 1)
        self.send(data)

    def _bcolor(self):
        """color from 8-8-8 to 5-6-5"""
        rgb = self.bcolor['R'] << 16 | self.bcolor['G'] << 8 | self.bcolor['B']
        return ((rgb & 0x00f80000) >> 8) | ((rgb & 0x0000fc00) >> 5) | ((rgb & 0x000000f8) >> 3)

    def _color(self):
        """color from 8-8-8 to 5-6-5"""
        rgb = self.color['R'] << 16 | self.color['G'] << 8 | self.color['B']
        return ((rgb & 0x00f80000) >> 8) | ((rgb & 0x0000fc00) >> 5) | ((rgb & 0x000000f8) >> 3)

    def init(self):
        """init display"""
        GPIO.output(self.pins['RST'], 1)
        time.sleep(0.005)
        GPIO.output(self.pins['RST'], 0)
        time.sleep(0.005)
        GPIO.output(self.pins['RST'], 1)
        time.sleep(0.005)

        # ************* ILI9325C/D **********
        self.cmd_data(0x0001, 0x0100)  # set SS and SM bit
        self.cmd_data(0x0002, 0x0200)  # set 1 line inversion
        self.cmd_data(0x0003, 0x1030)  # set GRAM write direction and BGR=1.
        self.cmd_data(0x0004, 0x0000)  # Resize register
        self.cmd_data(0x0008, 0x0207)  # set the back porch and front porch
        self.cmd_data(0x0009, 0x0000)  # set non-display area refresh cycle ISC[3:0]
        self.cmd_data(0x000A, 0x0000)  # FMARK function
        self.cmd_data(0x000C, 0x0000)  # RGB interface setting
        self.cmd_data(0x000D, 0x0000)  # Frame marker Position
        self.cmd_data(0x000F, 0x0000)  # RGB interface polarity

        # ************* Power On sequence ****************
        self.cmd_data(0x0010, 0x0000)  # SAP, BT[3:0], AP, DSTB, SLP, STB
        self.cmd_data(0x0011, 0x0007)  # DC1[2:0], DC0[2:0], VC[2:0]
        self.cmd_data(0x0012, 0x0000)  # VREG1OUT voltage
        self.cmd_data(0x0013, 0x0000)  # VDV[4:0] for VCOM amplitude
        self.cmd_data(0x0007, 0x0001)
        time.sleep(0.2)  # Dis-charge capacitor power voltage
        self.cmd_data(0x0010, 0x1690)  # SAP, BT[3:0], AP, DSTB, SLP, STB
        self.cmd_data(0x0011, 0x0227)  # Set DC1[2:0], DC0[2:0], VC[2:0]
        time.sleep(0.05)
        self.cmd_data(0x0012, 0x000D)
        time.sleep(0.05)
        self.cmd_data(0x0013, 0x1200)  # VDV[4:0] for VCOM amplitude
        self.cmd_data(0x0029, 0x000A)  # 04  VCM[5:0] for VCOMH
        self.cmd_data(0x002B, 0x000D)  # Set Frame Rate
        time.sleep(0.05)
        self.cmd_data(0x0020, 0x0000)  # GRAM horizontal Address
        self.cmd_data(0x0021, 0x0000)  # GRAM Vertical Address

        # ************* Adjust the Gamma Curve *************
        self.cmd_data(0x0030, 0x0000)
        self.cmd_data(0x0031, 0x0404)
        self.cmd_data(0x0032, 0x0003)
        self.cmd_data(0x0035, 0x0405)
        self.cmd_data(0x0036, 0x0808)
        self.cmd_data(0x0037, 0x0407)
        self.cmd_data(0x0038, 0x0303)
        self.cmd_data(0x0039, 0x0707)
        self.cmd_data(0x003C, 0x0504)
        self.cmd_data(0x003D, 0x0808)

        # ************* Set GRAM area *************
        self.cmd_data(0x0050, 0x0000)  # Horizontal GRAM Start Address
        self.cmd_data(0x0051, 0x00EF)  # Horizontal GRAM End Address
        self.cmd_data(0x0052, 0x0000)  # Vertical GRAM Start Address
        self.cmd_data(0x0053, 0x013F)  # Vertical GRAM Start Address
        self.cmd_data(0x0060, 0xA700)  # Gate Scan Line
        self.cmd_data(0x0061, 0x0001)  # NDL, VLE, REV
        self.cmd_data(0x006A, 0x0000)  # set scrolling line

        # ************* Partial Display Control *************
        self.cmd_data(0x0080, 0x0000)
        self.cmd_data(0x0081, 0x0000)
        self.cmd_data(0x0082, 0x0000)
        self.cmd_data(0x0083, 0x0000)
        self.cmd_data(0x0084, 0x0000)
        self.cmd_data(0x0085, 0x0000)

        # ************* Panel Control *************
        self.cmd_data(0x0090, 0x0010)
        self.cmd_data(0x0092, 0x0000)
        self.cmd_data(0x0007, 0x0133)  # 262K color and display ON

    def _set_area(self, x1, y1, x2, y2):
        """select area to work with"""
        self.cmd_data(0x0020, x1)
        self.cmd_data(0x0021, y1)
        self.cmd_data(0x0050, x1)
        self.cmd_data(0x0052, y1)
        self.cmd_data(0x0051, x2)
        self.cmd_data(0x0053, y2)
        self.cmd(0x0022)

    def draw_pixel(self, x, y):
        """draw one pixel"""
        self._set_area(x, y, x, y)
        self.data(self._color())

    def _draw_vertical_line(self, x, y, length):
        """draw vertical line"""
        self._set_area(x, y, x, y + length)
        for _ in itertools.repeat(None, length):
            self.data(self._color())

    def _draw_horizontal_line(self, x, y, length):
        """draw horizontal line"""
        self._set_area(x, y, x + length, y)
        for _ in itertools.repeat(None, length):
            self.data(self._color())

    def _calculate_steps(self, length, step, required_length):
        """calculate lineparts - helper"""
        steps = [length for _ in range(0, step)]
        if step * length < required_length:
            for idx in range(0, required_length - step * length):
                steps[idx] += 1

        return steps

    def _draw_diagonal_line(self, x1, y1, x2, y2):
        """draw diagonal line"""
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        if width > height:
            if x2 < x1:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            offset_y = 1 if y2 > y1 else -1
            offset_x = 1 if x2 > x1 else -1
            horizontal = True
            step = height
            length = width / step
            steps = self._calculate_steps(length, step, width)
        else:
            if y2 < y1:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            offset_y = 1 if y2 > y1 else -1
            offset_x = 1 if x2 > x1 else -1
            horizontal = False
            step = width
            length = height / step
            steps = self._calculate_steps(length, step, height)
        dy = 0
        dx = 0
        for idx, step in enumerate(steps):
            if horizontal:
                self._draw_horizontal_line(
                    x1 + dx,
                    y1 + (idx * offset_y),
                    step
                )
                dx += step * offset_x
            else:
                self._draw_vertical_line(
                    x1 + (idx * offset_x),
                    y1 + dy,
                    step
                )
                dy += step * offset_y

    def draw_line(self, x1, y1, x2, y2):
        """draw a line"""
        if x1 == x2:
            self._draw_vertical_line(x1, min(y1, y2), abs(y2 - y1))
        elif y1 == y2:
            self._draw_horizontal_line(min(x1, x2), y1, abs(x2 - x1))
        else:
            self._draw_diagonal_line(x1, y1, x2, y2)

