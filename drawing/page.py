import abc


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
            steps = [height-2]
            horizontal = False
            offset_x = offset_y = 0
        elif y1 == y2:
            steps = [width-1]
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
        pass

    def draw_circle(self, x, y, r):
        """draw a circle"""
        pass

    def draw_arc(self, x, y, radius, start, end):
        """draw an arc"""
        pass

    def fill_rect(self, x1, y1, x2, y2):
        """draw a filled rectangle"""
        pass

    def get_page_value(self, i, j):
        """returns value"""
        return self.buffer[i][j]

    @abc.abstractmethod
    def flush(self, force=None):
        """flush buffer to the screen"""
        pass
