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
        spi.max_speed_hz = 8000000 #1953000 #2000000 #125000 * (8+16+2) #1953000 #3900000 #15600000 #3900000 #244000
        spi.mode = 0 #SPI_MODE_0
        self.spi = spi

    def init(self):
        pass
        self.cmd(0xae)# //--turn off oled panel
        self.cmd(0x00)# //--set low column address
        self.cmd(0x10)# //--set high column address
        self.cmd(0x40)# //--set start line address
        self.cmd(0xb0)# //--set page address
        self.cmd(0x81)# //--set contrast control register
        self.cmd(0xff)
        self.cmd(0xa1) #//--set segment re-map 127 to 0   a0:0 to seg127
        self.cmd(0xa6)# //--set normal display
        self.cmd(0xc9)# //--set com(N-1)to com0  c0:com0 to com(N-1)
        self.cmd(0xa8)# //--set multiples ratio(1to64)
        self.cmd(0x3f) ##//--1/64 duty
        self.cmd(0xd3)# //--set display offset
        self.cmd(0x00)# //--not offset
        self.cmd(0xd5)# //--set display clock divide ratio/oscillator frequency
        self.cmd(0x80)# //--set divide ratio
        self.cmd(0xd9)# //--set pre-charge period
        self.cmd(0xf1)
        self.cmd(0xda)# //--set com pins hardware configuration
        self.cmd(0x12)
        self.cmd(0xdb) #//--set vcomh
        self.cmd(0x40)
        self.cmd(0x8d)# //--set chare pump enable/disable
        self.cmd(0x14)# //--set(0x10) disable
        self.cmd(0xaf)# //--turn on oled panel


    def cmd(self, data):
        GPIO.output(self.pins['DC'], 0)
        self.spi.xfer2([data])

    def data(self, data):
        GPIO.output(self.pins['DC'], 1)
        self.spi.xfer2([data])
        GPIO.output(self.pins['DC'], 0)

    def set_xy(self,width ,height):
        self.cmd(0x22)
        self.cmd(0xb0)              # Page start address. (0 = reset)
        self.cmd(0xb1 + (height//8 - 1)) # Page end address.

        self.cmd(0x21)
        self.cmd(0)              # Column start address. (0 = reset)
        self.cmd(width-1)   # Column end address.
        time.sleep(0.0025)

    def set_area(self, x, y):
        self.cmd(0x22)
        self.cmd(0xb0 + y)
        self.cmd(0xb0 + y +1)
        time.sleep(0.0025)
        self.cmd(0x21)
        self.cmd(0)
        self.cmd(x)

    def fill(self, c=0xff):
        for j in range(0, self.height//8):
            self.set_area(self.width-1, j)
            for i in range(0, self.width):
                self.data(c)


o = Oled(128, 64);
o.init()
o.fill(0)
o.fill(random.randint(0,255))


