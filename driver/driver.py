import abc


class Driver(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def init(self):
        """initialize a device"""
        pass

    @abc.abstractmethod
    def reset(self):
        """resets a device"""
        pass

    @abc.abstractmethod
    def cmd(self, data):
        """sends command to device"""
        pass

    @abc.abstractmethod
    def data(self, data):
        """sends data to device"""
        pass