"""Config parser fle"""
from configparser import ConfigParser
from importlib import import_module
import json


class Config(object):
    """Class Config"""
    def __init__(self, file="config.ini"):
        self.file = file
        self.config = ConfigParser()
        self.config.read(file)
        self.lcd = None
        self.touch = None
        self.init_lcd()

    def get(self, key, default=None):
        """returns value for key"""
        return self.config.get('general', key) if self.config.get('general', key) else default

    def get_section(self, section):
        """return section"""
        return dict(self.config.items(section))

    def init_lcd(self):
        """dynamically load and init lcd"""
        driver_name = self.config.get('lcd', 'driver')
        chip_name = self.config.get('lcd', 'lcd')
        size = self.config.get('lcd', 'size').split(",")
        driver_pins = self._get_dict(self.config.get('lcd', 'driver_pins'))

        path = "gfxlcd.driver.{}.{}".format(chip_name, driver_name)
        class_ = getattr(import_module(path), driver_name.upper())
        driver = class_()
        if driver_pins:
            driver.pins = driver_pins

        path = "gfxlcd.driver.{}.{}".format(chip_name, chip_name)
        class_ = getattr(import_module(path), chip_name.upper())
        self.lcd = class_(int(size[0]), int(size[1]), driver)
        self.lcd.rotation = int(self.config.get('lcd', 'rotate'))
        self.lcd.init()

    def init_touch(self, callback):
        """dynamically load and init touch panel"""
        driver_name = self.config.get('touch', 'driver')
        size = self.config.get('touch', 'size').split(",")
        cs = self.config.get('touch', 'cs')
        if cs == '':
            cs = None
        else:
            cs = int(self.config.get('touch', 'cs'))
        path = "gfxlcd.driver.{}.{}".format(driver_name, driver_name)
        class_ = getattr(import_module(path), driver_name.upper())
        driver = class_(
            int(size[0]), int(size[1]),
            int(self.config.get('touch', 'irq')),
            callback,
            cs
        )
        driver.rotate = int(self.config.get('touch', 'rotate'))
        driver.init()

    def _get_dict(self, value):
        """str to dict, replace '' with None"""
        if not value:
            return None
        values = json.loads(value)
        for key in values:
            if values[key] == "":
                values[key] = None

        return values
