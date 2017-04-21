import abc
import math


class Page(metaclass=abc.ABCMeta):
    """Page drawing algorithm"""
    def __init__(self):
        self.buffer = []

    def init(self):
        """init page"""
        self.buffer = [[0] * (self.height // 8) for x in range(self.width)]

    def draw_pixel(self, x, y):
        """draw a pixel at x,y"""
        self.buffer[x][y//8] |= 1 << (y % 8)
        self.flush()

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
                for appendix in range(int(step)+1):
                    self.draw_pixel(
                        int(x1 + dx + appendix),
                        int(y1 + (idx * offset_y))
                    )
                dx += step * offset_x
            else:
                for appendix in range(int(step)+1):
                    self.draw_pixel(
                        int(x1 + (idx * offset_x)),
                        int(y1 + dy + appendix)
                    )
                dy += step * offset_y

    def draw_rect(self, x1, y1, x2, y2):
        """draw a rectangle"""
        self.draw_line(x1, y1, x2, y1)
        self.draw_line(x1, y2, x2, y2)
        self.draw_line(x1, y1, x1, y2)
        self.draw_line(x2, y1, x2, y2)

    def draw_circle(self, x, y, radius):
        """draw a circle"""
        err = 0
        offset_x = radius
        offset_y = 0
        while offset_x >= offset_y:
            self.draw_pixel(x + offset_x, y + offset_y)
            self.draw_pixel(x + offset_y, y + offset_x)
            self.draw_pixel(x - offset_y, y + offset_x)
            self.draw_pixel(x - offset_x, y + offset_y)
            self.draw_pixel(x - offset_x, y - offset_y)
            self.draw_pixel(x - offset_y, y - offset_x)
            self.draw_pixel(x + offset_y, y - offset_x)
            self.draw_pixel(x + offset_x, y - offset_y)
            if err <= 0:
                offset_y += 1
                err += 2*offset_y + 1
            else:
                offset_x -= 1
                err -= 2*offset_x + 1

    def draw_arc(self, x, y, radius, start, end):
        """draw an arc"""
        start = start * math.pi / 180
        end = end * math.pi / 180

        err = 0
        offset_x = radius
        offset_y = 0
        while offset_x >= offset_y:
            if start <= math.atan2(offset_y, offset_x) <= end:
                self.draw_pixel(x + offset_x, y + offset_y)
            if start <= math.atan2(offset_x, offset_y) <= end:
                self.draw_pixel(x + offset_y, y + offset_x)
            if start <= math.atan2(offset_x, -offset_y) <= end:
                self.draw_pixel(x - offset_y, y + offset_x)
            if start <= math.atan2(offset_y, -offset_x) <= end:
                self.draw_pixel(x - offset_x, y + offset_y)

            if start <= math.atan2(-offset_y, -offset_x) + 2*math.pi <= end:
                self.draw_pixel(x - offset_x, y - offset_y)
            if start <= math.atan2(-offset_x, -offset_y) + 2*math.pi <= end:
                self.draw_pixel(x - offset_y, y - offset_x)
            if start <= math.atan2(-offset_x, offset_y) + 2*math.pi <= end:
                self.draw_pixel(x + offset_y, y - offset_x)
            if start <= math.atan2(-offset_y, offset_x) + 2*math.pi <= end:
                self.draw_pixel(x + offset_x, y - offset_y)

            if err <= 0:
                offset_y += 1
                err += 2*offset_y + 1
            else:
                offset_x -= 1
                err -= 2*offset_x + 1

    def fill_rect(self, x1, y1, x2, y2):
        """draw a filled rectangle"""
        if y2 < y1:
            y1, y2 = y2, y1
        if x2 < x1:
            x1, x2 = x2, x1
        start_page = y1 // 8
        start_bit = y1 % 8
        end_page = y2 // 8
        end_bit = y2 % 8
        rows = []
        first_page = int(('0' * start_bit).rjust(8, '1'), 2)
        last_page = int('1' * (end_bit+1), 2)
        if start_page != end_page:
            rows.append(first_page)
            for _ in range(end_page - start_page - 1):
                rows.append(255)
            rows.append(last_page)
        else:
            rows.append(first_page & last_page)

        page = start_page
        for v in rows:
            for x in range(x2-x1+1):
                self.buffer[x1+x][page] |= v
            page += 1

    def get_page_value(self, column, page):
        """returns value"""
        return self.buffer[column][page]

    @abc.abstractmethod
    def flush(self, force=None):
        """flush buffer to the screen"""
        pass
