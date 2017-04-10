import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
import spidev
import random


class Oled(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pins = {
            'RST': 13,
            'DC': 6,
        }

        for pin in self.pins:
            GPIO.setup(self.pins[pin], GPIO.OUT)
            GPIO.output(self.pins[pin], 0)

        spi = spidev.SpiDev()
        spi.open(0,0)
        spi.max_speed_hz = 8000000
        spi.mode = 0
        self.spi = spi

    def init(self):
        GPIO.output(self.pins['RST'], 1)
        time.sleep(0.025)
        GPIO.output(self.pins['RST'], 0)
        time.sleep(0.025)
        GPIO.output(self.pins['RST'], 1)
        time.sleep(0.025)
        self.cmd(0xae)  # turn off panel
        self.cmd(0x00)  # set low column address
        self.cmd(0x10)  # set high column address
        self.cmd(0x40)  # set start line address

        self.cmd(0x20)  # addr mode
        self.cmd(0x02)  # horizontal

        self.cmd(0xb0)  # set page address
        self.cmd(0x81)  # set contrast control register
        self.cmd(0xff)
        self.cmd(0xa1)  # a0/a1 set segment re-map 127 to 0   a0:0 to seg127
        self.cmd(0xc8)  # c8/c0 set com(N-1)to com0  c0:com0 to com(N-1)
        self.cmd(0xa6)  # set normal display, a6 - normal, a7 - inverted

        self.cmd(0xa8)  # set multiplex ratio(16to63)
        self.cmd(0x3f)  # 1/64 duty

        self.cmd(0xd3)  # set display offset
        self.cmd(0x00)  # not offset

        self.cmd(0xd5)  # set display clock divide ratio/oscillator frequency
        self.cmd(0x80)  # set divide ratio

        self.cmd(0xd9)  # set pre-charge period
        self.cmd(0xf1)
        self.cmd(0xda)  # set com pins hardware configuration
        self.cmd(0x12)

        self.cmd(0xdb)  # set vcomh
        self.cmd(0x40)

        self.cmd(0x8d)  # charge pump
        self.cmd(0x14)  # enable charge pump
        self.cmd(0xaf)  # turn on panel

    def cmd(self, data):
        GPIO.output(self.pins['DC'], 0)
        self.spi.xfer2([data])

    def data(self, data):
        GPIO.output(self.pins['DC'], 1)
        self.spi.xfer2([data])
        GPIO.output(self.pins['DC'], 0)

    def set_area(self, x1, y1, x2, y2):
        self.cmd(0x22)
        self.cmd(0xb0 + y1)
        self.cmd(0xb0 + y2)
        self.cmd(0x21)
        self.cmd(x1)
        self.cmd(x2)

    def fill(self, c=0xff):
        for j in range(0, self.height//8):
            self.set_area(0, j, self.width-1, j+1)
            for i in range(0, self.width):
                self.data(c)

    def draw_pixels(self, x, y, c=0xff):
        """draw a pixel /line"""
        j = y//8
        self.set_area(x, j, x+1, j+1)
        self.data(c)

o = Oled(128, 64)
o.init()
o.fill(0)

# o.fill(random.randint(0, 255))

o.draw_pixels(2, 0, 128)
o.draw_pixels(3, 0, 128)
o.draw_pixels(7, 0, 128)
o.draw_pixels(8, 0, 128)
o.draw_pixels(1, 9, 7)
o.draw_pixels(9, 9, 7)
o.draw_pixels(2, 9, 8)
o.draw_pixels(3, 9, 16)
o.draw_pixels(4, 9, 33)
o.draw_pixels(5, 9, 66)
o.draw_pixels(6, 9, 33)
o.draw_pixels(7, 9, 16)
o.draw_pixels(8, 9, 8)

o.draw_pixels(15, 9, 127)
o.draw_pixels(16, 9, 65)
o.draw_pixels(17, 9, 65)
o.draw_pixels(18, 9, 62)

o.draw_pixels(20, 9, 38)
o.draw_pixels(21, 9, 73)
o.draw_pixels(22, 9, 73)
o.draw_pixels(23, 9, 50)

o.draw_pixels(25, 9, 127)
o.draw_pixels(26, 9, 9)
o.draw_pixels(27, 9, 9)
o.draw_pixels(28, 9, 6)

o.draw_pixels(30, 9, 98)
o.draw_pixels(31, 9, 81)
o.draw_pixels(32, 9, 73)
o.draw_pixels(33, 9, 70)

o.draw_pixels(35, 9, 62)
o.draw_pixels(36, 9, 65)
o.draw_pixels(37, 9, 65)
o.draw_pixels(38, 9, 62)

o.draw_pixels(40, 9, 4)
o.draw_pixels(41, 9, 2+64)
o.draw_pixels(42, 9, 127)
o.draw_pixels(43, 9, 64)

o.draw_pixels(40, 9, 4)
o.draw_pixels(41, 9, 2+64)
o.draw_pixels(42, 9, 127)
o.draw_pixels(43, 9, 64)

o.draw_pixels(45, 9, 97)
o.draw_pixels(46, 9, 25)
o.draw_pixels(47, 9, 5)
o.draw_pixels(48, 9, 3)

