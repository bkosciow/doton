"""An abstract for Worker class"""
import abc


class Worker(metaclass=abc.ABCMeta):
    """Widget abstract"""
    @abc.abstractmethod
    def execute(self):
        """call a worker"""
        pass

    @abc.abstractmethod
    def start(self):
        """call a worker"""
        pass

    @abc.abstractmethod
    def shutdown(self):
        """stops worker and all services"""
        pass
