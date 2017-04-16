import sys
sys.path.append("../")
from drawing.page import Page
from driver.chip import Chip


class SSD1306(Page, Chip):
    """Class for an LCD with SSD306 chip"""
    def __init__(self, width, height, driver, auto_flush=True):
        Page.__init__(self)
        Chip.__init__(self, width, height, driver, auto_flush)

    def init(self):
        """inits a device"""
        self.driver.init()
        Page.init(self)
        Chip.init(self)
        self.driver.reset()
        self.driver.cmd(0xae)  # turn off panel
        self.driver.cmd(0x00)  # set low column address
        self.driver.cmd(0x10)  # set high column address
        self.driver.cmd(0x40)  # set start line address

        self.driver.cmd(0x20)  # addr mode
        self.driver.cmd(0x02)  # horizontal

        self.driver.cmd(0xb0)  # set page address
        self.driver.cmd(0x81)  # set contrast control register
        self.driver.cmd(0xff)
        self.driver.cmd(0xa1)  # a0/a1 set segment re-map 127 to 0   a0:0 to seg127
        self.driver.cmd(0xc8)  # c8/c0 set com(N-1)to com0  c0:com0 to com(N-1)
        self.driver.cmd(0xa6)  # set normal display, a6 - normal, a7 - inverted

        self.driver.cmd(0xa8)  # set multiplex ratio(16to63)
        self.driver.cmd(0x3f)  # 1/64 duty

        self.driver.cmd(0xd3)  # set display offset
        self.driver.cmd(0x00)  # not offset

        self.driver.cmd(0xd5)  # set display clock divide ratio/oscillator frequency
        self.driver.cmd(0x80)  # set divide ratio

        self.driver.cmd(0xd9)  # set pre-charge period
        self.driver.cmd(0xf1)
        self.driver.cmd(0xda)  # set com pins hardware configuration
        self.driver.cmd(0x12)

        self.driver.cmd(0xdb)  # set vcomh
        self.driver.cmd(0x40)

        self.driver.cmd(0x8d)  # charge pump
        self.driver.cmd(0x14)  # enable charge pump
        self.driver.cmd(0xaf)  # turn on panel

    def flush(self, force=None):
        """flush buffer to device
        :force - boolean|None"""
        if force is None:
            force = self.options['auto_flush']

        if force:
            for j in range(0, self.height//8):
                self.set_area(0, j, self.width-1, j+1)
                for i in range(0, self.width):
                    self.driver.data(self.get_page_value(i, j))

    def set_area(self, x1, y1, x2, y2):
        """set area to work on"""
        self.driver.cmd(0x22)
        self.driver.cmd(0xb0 + y1)
        self.driver.cmd(0xb0 + y2)
        self.driver.cmd(0x21)
        self.driver.cmd(x1)
        self.driver.cmd(x2)
    #
    # def fill(self, c=0xff):
    #     for j in range(0, self.height//8):
    #         self.set_area(0, j, self.width-1, j+1)
    #         for i in range(0, self.width):
    #             self.driver.data(c)
    #