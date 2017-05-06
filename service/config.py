"""Config parser fle"""
from configparser import ConfigParser


class Config(object):
    """Class Config"""
    def __init__(self, file="config.ini"):
        self.file = file
        self.config = ConfigParser()
        self.config.read(file)

    def get(self, key, default=None):
        """returns value for key"""
        return self.config.get('general', key) if self.config.get('general', key) else default
