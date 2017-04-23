from drawing.pixel import Pixel
import itertools


class Area(Pixel):
    """Page drawing algorithm"""
    def __init__(self):
        Pixel.__init__(self)

    def init(self):
        pass

    def draw_pixel(self, x, y):
        """draw one pixel"""
        self._set_area(x, y, x, y)
        self.driver.data(self._converted_color(), None)

    def _set_area(self, x1, y1, x2, y2):
        """select area to work with"""
        self.driver.cmd_data(0x0020, x1)
        self.driver.cmd_data(0x0021, y1)
        self.driver.cmd_data(0x0050, x1)
        self.driver.cmd_data(0x0052, y1)
        self.driver.cmd_data(0x0051, x2)
        self.driver.cmd_data(0x0053, y2)
        self.driver.cmd(0x0022, None)


    def _draw_vertical_line(self, x, y, length):
        """draw vertical line"""
        self._set_area(x, y, x, y + length)
        color = self._converted_color()
        for _ in itertools.repeat(None, length):
            self.driver.data(color, None)

    def _draw_horizontal_line(self, x, y, length):
        """draw horizontal line"""
        self._set_area(x, y, x + length, y)
        color = self._converted_color()
        for _ in itertools.repeat(None, length):
            self.driver.data(color, None)

    def _calculate_steps(self, length, step, required_length):
        """calculate lineparts - helper"""
        steps = [length for _ in range(0, step)]
        if step * length < required_length:
            for idx in range(0, required_length - step * length):
                steps[idx] += 1

        return steps

    def draw_line(self, x1, y1, x2, y2):
        """draw diagonal line"""
        width = abs(x2 - x1)
        height = abs(y2 - y1)
        if x1 == x2:
            steps = [height]
            horizontal = False
            offset_x = offset_y = 0
        elif y1 == y2:
            steps = [width]
            horizontal = True
            offset_x = offset_y = 0
        elif width > height:
            if x2 < x1:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            offset_y = 1 if y2 > y1 else -1
            offset_x = 1 if x2 > x1 else -1
            horizontal = True
            step = height
            length = width / step
            steps = self._calculate_steps(length, step, width)

        else:
            if y2 < y1:
                x1, x2 = x2, x1
                y1, y2 = y2, y1
            offset_y = 1 if y2 > y1 else -1
            offset_x = 1 if x2 > x1 else -1
            horizontal = False
            step = width
            length = height / step
            steps = self._calculate_steps(length, step, height)

        dy = 0
        dx = 0
        for idx, step in enumerate(steps):
            if horizontal:
                self._draw_horizontal_line(
                    int(x1 + dx),
                    int(y1 + (idx * offset_y)),
                    int(step)
                )
                dx += step * offset_x
            else:
                self._draw_vertical_line(
                    int(x1 + (idx * offset_x)),
                    int(y1 + dy),
                    int(step)
                )
                dy += step * offset_y

    def fill_rect(self, x1, y1, x2, y2):
        """fill an area"""
        size = abs(x2 - x1) * abs(y2 - y1)
        self._set_area(
            min(x1, x2),
            min(y1, y2),
            max(x1, x2)-1,
            max(y1, y2)-1
        )
        color = self._converted_background_color()
        for _ in range(0, size):
            self.driver.data(color, None)
