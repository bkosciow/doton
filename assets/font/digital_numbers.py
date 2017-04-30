"""Font for numbers"""
from PIL import Image


class DigitalNumbers(object):
    """Digital font class"""
    def __init__(self):
        self.resource = Image.open("assets/font/digital_numbers.jpg")
        self.offsets = {
            0: 0,
            1: 24,
            2: 48,
            3: 72,
            4: 96,
            5: 120,
            6: 144,
            7: 168,
            8: 192,
            9: 216
        }
        self.loaded_resources = {}

    def get(self, item):
        """get image reference"""
        if item not in self.loaded_resources:
            self.load_resource(item)

        return self.loaded_resources[item]

    def load_resource(self, number):
        """create reference to single number"""
        area = (self.offsets[number], 0, self.offsets[number] + 24, 42)
        self.loaded_resources[number] = self.resource.crop(area)

    def get_transparency(self):
        """get font transparency"""
        return ((1, 1, 1), (9, 9, 9))
