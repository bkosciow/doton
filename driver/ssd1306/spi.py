import RPi.GPIO as GPIO
import spidev
GPIO.setmode(GPIO.BCM)
import time
from driver.driver import Driver


class SPI(Driver):
    def __init__(self):
        self.pins = {
            'RST': 13,
            'DC': 6,
        }
        self.spi = None

    def init(self):
        for pin in self.pins:
            GPIO.setup(self.pins[pin], GPIO.OUT)
            GPIO.output(self.pins[pin], 0)

        spi = spidev.SpiDev()
        spi.open(0,0)
        spi.max_speed_hz = 8000000
        spi.mode = 0
        self.spi = spi

    def reset(self):
        GPIO.output(self.pins['RST'], 1)
        time.sleep(0.025)
        GPIO.output(self.pins['RST'], 0)
        time.sleep(0.025)
        GPIO.output(self.pins['RST'], 1)
        time.sleep(0.025)

    def cmd(self, data):
        GPIO.output(self.pins['DC'], 0)
        self.spi.xfer2([data])

    def data(self, data):
        GPIO.output(self.pins['DC'], 1)
        self.spi.xfer2([data])
        GPIO.output(self.pins['DC'], 0)

