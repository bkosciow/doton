import threading
import time


class WidgetHolder(object):
    """Widget Holder"""
    def __init__(self, coords, widget):
        self.coords = coords
        self.widget = widget


class WindowManager(threading.Thread):
    """Window Manager"""
    def __init__(self, lcd):
        threading.Thread.__init__(self)
        self.widgets = {}
        self.lcd = lcd
        self.work = True

    def add_widget(self, name, coordinates, widget, page=0):
        """add widget to grid, calculate (x,y)"""
        position = []
        for coords in coordinates:
            position.append((coords[0]*134, coords[1]*106))

        self.widgets[name] = WidgetHolder(position, widget)

    def run(self):
        """main loop - drawing"""
        for holder in self.widgets:
            self.widgets[holder].widget.draw_widget(self.lcd, self.widgets[holder].coords)
        while self.work:
            for holder in self.widgets:
                self.widgets[holder].widget.draw_values(self.lcd, self.widgets[holder].coords)
            time.sleep(0.025)

    def stop(self):
        """stops a thread"""
        self.work = False

    def set_widget_color(self, name, key, value):
        """change colour"""
        self.widgets[name].widget.colours[key] = value

    def get_widget(self, name):
        """get widget by name"""
        return self.widgets[name].widget

    def get_widgets(self):
        """returns widgets dictionary"""
        widgets = {}
        for hanlder in self.widgets:
            widgets[hanlder] = self.widgets[hanlder].widget

        return widgets
