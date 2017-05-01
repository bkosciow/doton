"""Font for numbers"""
from PIL import Image


class Numbers(object):
    """Digital font class"""
    def __init__(self):
        self.resource = Image.open("assets/font/digital_numbers_30.png")
        self.offsets = {
            0: 0,
            1: 17,
            2: 34,
            3: 51,
            4: 68,
            5: 85,
            6: 102,
            7: 119,
            8: 136,
            9: 153
        }
        self.loaded_resources = {}

    def get(self, item):
        """get image reference"""
        if item not in self.loaded_resources:
            self.load_resource(item)

        return self.loaded_resources[item]

    def load_resource(self, number):
        """create reference to single number"""
        area = (self.offsets[number], 0, self.offsets[number] + 16, 29)
        self.loaded_resources[number] = self.resource.crop(area)

    def get_transparency(self):
        """get font transparency"""
        return ((1, 1, 1), (0, 0, 0))
