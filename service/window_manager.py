import threading
import time


class WindowManager(threading.Thread):
    """Window Manager"""
    def __init__(self, lcd):
        threading.Thread.__init__(self)
        self.widgets = {}
        self.lcd = lcd
        self.work = True

    def add_widget(self, name, widget, page=0):
        """add widget to grid, calculate (x,y)"""
        position = []
        for coords in widget.coords:
            position.append((coords[0]*134, coords[1]*106))
        widget.coords = position
        self.widgets[name] = widget

    def run(self):
        """main loop - drawing"""
        for widget in self.widgets:
            self.widgets[widget].draw_widget(self.lcd)
        while self.work:
            for widget in self.widgets:
                self.widgets[widget].draw_values(self.lcd)
            time.sleep(0.025)

    def stop(self):
        """stops a thread"""
        self.work = False

    def set_widget_color(self, name, key, value):
        """change colour"""
        self.widgets[name].colours[key] = value

    def get_widget(self, name):
        """get widget by name"""
        return self.widgets[name]
