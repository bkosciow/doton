"""Window Manager"""
import threading
import time


class WidgetHolder(object):
    """Widget Holder"""
    def __init__(self, coords, widget):
        self.coords = coords
        self.widget = widget


class Page(object):
    """Page class"""
    def __init__(self):
        self.widgets = {}


class WindowManager(threading.Thread):
    """Window Manager"""
    def __init__(self, lcd):
        threading.Thread.__init__(self)
        self.pages = [Page()]
        self.active_page = 0
        self.lcd = lcd
        self.work = True

    def add_widget(self, name, coordinates, widget, page=0):
        """add widget to grid, calculate (x,y)"""
        position = []
        for coords in coordinates:
            position.append((coords[0]*134, coords[1]*106))

        self.pages[page].widgets[name] = WidgetHolder(position, widget)

    def run(self):
        """main loop - drawing"""
        widgets = self.pages[self.active_page].widgets
        for holder in widgets:
            widgets[holder].widget.draw_widget(
                self.lcd, widgets[holder].coords
            )
        while self.work:
            for holder in widgets:
                widgets[holder].widget.draw_values(
                    self.lcd, widgets[holder].coords
                )
            time.sleep(0.025)

    def stop(self):
        """stops a thread"""
        self.work = False

    def set_widget_color(self, name, key, value):
        """change colour"""
        self.pages[self.active_page].widgets[name].widget.colours[key] = value

    def get_widget(self, name):
        """get widget by name"""
        return self.pages[self.active_page].widgets[name].widget

    def get_widgets(self):
        """returns widgets dictionary"""
        widgets = self.pages[self.active_page].widgets
        return_widgets = {}
        for hanlder in widgets:
            return_widgets[hanlder] = widgets[hanlder].widget

        return return_widgets
