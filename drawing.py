import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
from driver.nju6450.gpio import GPIO
from driver.nju6450.nju6450 import NJU6450
from driver.ssd1306.spi import SPI
from driver.ssd1306.ssd1306 import SSD1306
from driver.ili9325.gpio import GPIO as ILIGPIO
from driver.ili9325.ili9325 import ILI9325

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

lcd_tft = ILI9325(240, 320, ILIGPIO())
lcd_tft.init()
#
# lcd_nju.draw_circle(60, 15, 15)
# lcd_nju.draw_circle(53, 10, 3)
# lcd_nju.draw_circle(67, 10, 3)
# lcd_nju.draw_arc(60, 15, 10, 45, 135)
# lcd_nju.draw_line(60, 12, 57, 17)
# lcd_nju.draw_line(60, 12, 63, 17)
# lcd_nju.draw_arc(60, 15, 3, 45, 135)
#
# lcd_nju.fill_rect(2, 2, 42, 29)
# lcd_nju.fill_rect(119, 2, 109, 12)
# lcd_nju.fill_rect(119, 17, 109, 19)
#
# lcd_nju.draw_rect(77, 6, 105, 16)
# lcd_nju.fill_rect(77, 16, 105, 25)
#
#
# lcd_oled.draw_circle(31, 32, 31)
# lcd_oled.draw_circle(19, 22, 7)
# lcd_oled.draw_circle(43, 22, 7)
# lcd_oled.draw_arc(31, 32, 20, 45, 135)
# lcd_oled.draw_line(31, 27, 27, 38)
# lcd_oled.draw_line(31, 27, 35, 38)
# lcd_oled.draw_arc(31, 35, 5, 45, 135)
#
# lcd_oled.fill_rect(95, 4, 105, 10)
# lcd_oled.draw_rect(80, 10, 120, 25)
# lcd_oled.fill_rect(80, 26, 120, 59)
#
# lcd_oled.flush(True)
# lcd_nju.flush(True)

# bypass of missing +3v line to power backlight
LED = 6
RPi.GPIO.setup(LED, RPi.GPIO.OUT)
RPi.GPIO.output(LED, 1)
lcd_tft.background_color = (255, 255, 255)
lcd_tft.fill_rect(0, 0, 240, 320)
lcd_tft.color = (0, 255, 1)
lcd_tft.draw_circle(79, 99, 40)
lcd_tft.draw_circle(60, 80, 7)
lcd_tft.draw_circle(100, 80, 7)

lcd_tft.draw_line(79, 90, 70, 100)
lcd_tft.draw_line(79, 90, 88, 100)
lcd_tft.draw_arc(79, 91, 12, 45, 135)

lcd_tft.color = (255, 0, 0)
lcd_tft.draw_arc(79, 90, 40, 45, 135)
lcd_tft.draw_line(51, 117, 105, 117)

lcd_tft.background_color = (255, 127, 127)
lcd_tft.fill_rect(75, 140, 83, 220)
lcd_tft.draw_line(75, 220, 65, 280)
lcd_tft.draw_line(83, 220, 93, 280)
lcd_tft.draw_line(83, 150, 130, 150)

lcd_tft.background_color = (0, 255, 0)
lcd_tft.fill_rect(0, 0, 122, 32)
lcd_tft.color = (0, 0, 0)
lcd_tft.background_color = (0, 0, 0)
lcd_tft.draw_circle(60, 15, 15)
lcd_tft.draw_circle(53, 10, 3)
lcd_tft.draw_circle(67, 10, 3)
lcd_tft.draw_arc(60, 15, 10, 45, 135)
lcd_tft.draw_line(60, 12, 57, 17)
lcd_tft.draw_line(60, 12, 63, 17)
lcd_tft.draw_arc(60, 15, 3, 45, 135)
lcd_tft.fill_rect(2, 2, 42, 29)
lcd_tft.fill_rect(119, 2, 109, 12)
lcd_tft.fill_rect(119, 17, 109, 19)
lcd_tft.draw_rect(77, 6, 105, 16)
lcd_tft.fill_rect(77, 16, 105, 25)

lcd_tft.background_color = (0, 0, 0)
lcd_tft.fill_rect(100, 200, 222, 264)
lcd_tft.color = (43, 212, 255)
lcd_tft.background_color = (43, 212, 255)
lcd_tft.draw_circle(131, 232, 31)
lcd_tft.draw_circle(119, 222, 7)
lcd_tft.draw_circle(143, 222, 7)
lcd_tft.draw_arc(131, 232, 20, 45, 135)
lcd_tft.draw_line(131, 227, 127, 238)
lcd_tft.draw_line(131, 227, 135, 238)
lcd_tft.draw_arc(131, 235, 5, 45, 135)
lcd_tft.fill_rect(195, 204, 205, 210)
lcd_tft.draw_rect(180, 210, 220, 225)
lcd_tft.fill_rect(180, 226, 220, 259)