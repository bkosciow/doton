"""Window Manager"""
import threading
import time
from view.widget import Clickable


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
        self.widgets = None
        self.draw_page = True

    def add_widget(self, name, coordinates, widget, page=0):
        """add widget to grid, calculate (x,y)"""
        position = []
        for coords in coordinates:
            position.append((coords[0]*134, coords[1]*106))
        if page > len(self.pages)-1:
            self._add_page(page)
        self.pages[page].widgets[name] = WidgetHolder(position, widget)

    def _add_page(self, page):
        """add new page"""
        if len(self.pages) < page:
            raise Exception('Cannot create page '+str(page))

        self.pages.append(Page())

    def run(self):
        """main loop - drawing"""
        self.widgets = self.pages[self.active_page].widgets
        while self.work:
            if self.draw_page:
                self._draw_widgets()
            for holder in self.widgets:
                self.widgets[holder].widget.draw_values(
                    self.lcd, self.widgets[holder].coords
                )
            time.sleep(0.025)

    def _draw_widgets(self):
        """draw widgets"""
        self.lcd.background_color = (0, 0, 0)
        self.lcd.fill_rect(0, 0, self.lcd.width, self.lcd.height)
        for holder in self.widgets:
            self.widgets[holder].widget.draw_widget(
                self.lcd, self.widgets[holder].coords
            )
        self.lcd.background_color = (255, 255, 255)
        self.lcd.fill_rect(75, 0, 165, 60)
        self.lcd.fill_rect(75, 260, 165, 320)
        self.draw_page = False

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
        return_widgets = {}
        for page in self.pages:
            widgets = page.widgets
            for handler in widgets:
                return_widgets[handler] = widgets[handler].widget

        return return_widgets

    def click(self, point):
        """execute click event"""
        if self._execute_internal_event(point):
            return
        pos_x, pos_y = point
        holders = self.pages[self.active_page].widgets
        found = (None, None)
        for name in holders:
            idx = 0
            if isinstance(holders[name].widget, Clickable):
                for coords in holders[name].coords:
                    if coords[0] < pos_x < coords[0] + 134 and coords[1] < pos_y < coords[1] + 106:
                        found = (name, idx, pos_x - coords[0], pos_y - coords[1])
                        break
                    idx += 1

        if all(val is not None for val in found):
            self.pages[self.active_page].widgets[found[0]].widget.action(*found)

    def _execute_internal_event(self, point):
        """execute internal event"""
        if 75 < point[0] < 165 and 0 < point[1] < 60:
            self._page_previous()
            return True
        if 75 < point[0] < 165 and 260 < point[1] < 320:
            self._page_next()
            return True
        return False

    def _page_previous(self):
        """switch to prev page"""
        if self.active_page > 0:
            print("prev")
            self.widgets = self.pages[self.active_page-1].widgets
            self.draw_page = True
            self.active_page -= 1

    def _page_next(self):
        """switch to next page"""
        if self.active_page < len(self.pages)-1:
            print("next")
            self.widgets = self.pages[self.active_page+1].widgets
            self.draw_page = True
            self.active_page += 1
