"""Window manager holder"""


class WidgetHolder(object):
    """Widget Holder"""
    def __init__(self, coords, slots, widget):
        self.coords = coords
        self.slots = slots
        self.widget = widget
