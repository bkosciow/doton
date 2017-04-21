from driver.nju6450.gpio import GPIO
from driver.nju6450.nju6450 import NJU6450
from driver.ssd1306.spi import SPI
from driver.ssd1306.ssd1306 import SSD1306
import random

def hole(o, x, y):
    o.draw_pixel(x+1, y)
    o.draw_pixel(x+2, y)
    o.draw_pixel(x+3, y)
    o.draw_pixel(x+1, y + 4)
    o.draw_pixel(x+2, y + 4)
    o.draw_pixel(x+3, y + 4)
    o.draw_pixel(x, y + 1)
    o.draw_pixel(x+4, y + 1)
    o.draw_pixel(x, y + 2)
    o.draw_pixel(x+4, y + 2)
    o.draw_pixel(x, y + 3)
    o.draw_pixel(x+4, y + 3)

def draw_points(o):
    for _ in range(0, 50):
        hole(o, random.randint(2,o.width - 10), random.randint(2,o.height-10))

def draw_net(o):
    s = 0
    while s < o.width-1:
        o.draw_line(s, 0, s, o.height-1)
        s += 10
    s = 0
    while s < o.height-1:
        o.draw_line(0, s, o.width-1, s)
        s += 10

lcd_oled = SSD1306(128, 64, SPI())
lcd_oled.init()
lcd_oled.auto_flush = False

lcd_nju = NJU6450(122, 32, GPIO())
lcd_nju.init()
lcd_nju.auto_flush = False

# lcd_oled.draw_line(0, 0, lcd_oled.width-1, lcd_oled.height-1)
# lcd_oled.draw_line(0, lcd_oled.height-1, lcd_oled.width-1, 0)

# draw_net(lcd_oled)
# draw_net(lcd_nju)
#draw_points(lcd_oled)
#draw_points(lcd_nju)

# lcd_nju.draw_line(0, 0, lcd_nju.width-1, lcd_nju.height-1)
# lcd_nju.draw_line(0, lcd_nju.height-1, lcd_nju.width-1, 0)

# lcd_nju.draw_rect(10, 10, 40, 30)
# lcd_oled.draw_rect(10, 10, 40, 40)

lcd_nju.draw_circle(60, 15, 15)
lcd_nju.draw_circle(53, 10, 3)
lcd_nju.draw_circle(67, 10, 3)
lcd_nju.draw_arc(60, 15, 10, 45, 135)
lcd_nju.draw_line(60, 12, 57, 17)
lcd_nju.draw_line(60, 12, 63, 17)
lcd_nju.draw_arc(60, 15, 3, 45, 135)

lcd_nju.fill_rect(2, 2, 42, 29)
lcd_nju.fill_rect(119, 2, 109, 12)
lcd_nju.fill_rect(119, 17, 109, 19)

lcd_nju.draw_rect(77, 6, 105, 16)
lcd_nju.fill_rect(77, 16, 105, 25)


lcd_oled.draw_circle(31, 32, 31)
lcd_oled.draw_circle(19, 22, 7)
lcd_oled.draw_circle(43, 22, 7)
lcd_oled.draw_arc(31, 32, 20, 45, 135)
lcd_oled.draw_line(31, 27, 27, 38)
lcd_oled.draw_line(31, 27, 35, 38)
lcd_oled.draw_arc(31, 35, 5, 45, 135)

lcd_oled.fill_rect(95, 4, 105, 10)
lcd_oled.draw_rect(80, 10, 120, 25)
lcd_oled.fill_rect(80, 26, 120, 59)

lcd_oled.flush(True)
lcd_nju.flush(True)
