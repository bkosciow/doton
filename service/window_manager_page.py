"""Window manager page"""


class Page(object):
    """Page class"""
    def __init__(self, size):
        self.size = size
        self.widgets = {}

    def add_widget(self, name, widget_holder):
        """add widget holder to page"""
        if self.validate_slot(widget_holder.slots):
            self.widgets[name] = widget_holder
        else:
            raise AttributeError('one or more slots in use ', widget_holder.slots)

    def validate_slot(self, slots):
        """checks if given slots are empty"""
        for slot in slots:
            for widget in self.widgets:
                if slot in self.widgets[widget].slots:
                    return False

        return True
