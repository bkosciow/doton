

class Page(object):
    """Page drawing algorithm"""
    def __init__(self):
        self.buffer = []

    def init(self):
        """init page"""
        #self.buffer = [[0] * (self.height // 8) for x in range(self.width)]
        self.buffer = [[0] * (self.height // 8) for x in range(self.width)]

    def draw_pixel(self, x, y):
        """draw a pixel at x,y"""
        self.buffer[x][y//8] |= 1 << (y % 8)
        self.flush()

    def draw_line(self, x1, y1, x2, y2):
        """draw a line from point x1,y1 to x2,y2"""
        pass

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
