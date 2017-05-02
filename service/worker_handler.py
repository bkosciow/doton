"""Handler for workers"""
import threading
import time


class Job(object):
    """Class Job"""
    def __init__(self, worker, frequency):
        self.worker = worker
        self.worker.start()
        self.frequency = frequency
        self.tick = 0

    def can_execute(self):
        """checks if it is time to execute worker"""
        self.tick += 1
        if self.tick == self.frequency:
            self.tick = 0
            return True
        return False

    def execute(self):
        """executes a worker"""
        self.worker.execute()

    def shutdown(self):
        """shutdown worker"""
        self.worker.shutdown()


class Handler(threading.Thread):
    """Handler class"""
    def __init__(self):
        threading.Thread.__init__(self)
        self.workers = {}
        self.tick = 1
        self.work = True

    def add(self, name, worker, frequency):
        """add worker to pool"""
        self.workers[name] = Job(worker, frequency)

    def run(self):
        """main loop"""
        while self.work:
            for worker in self.workers:
                if self.workers[worker].can_execute():
                    self.workers[worker].execute()
            time.sleep(1)

    def stop(self):
        """stops a thread"""
        self.work = False
        for worker in self.workers:
            self.workers[worker].shutdown()
