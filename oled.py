from driver.ssd1306.spi import SPI
from driver.ssd1306.ssd1306 import SSD1306

drv = SPI()
o = SSD1306(128, 64, drv)

o.init()
o.draw_pixel(5, 0)
o.draw_pixel(6, 1)
o.draw_pixel(7, 2)
o.draw_pixel(5, 3)
# o.fill(0)
#
# o.fill(random.randint(0, 255))
#
# o.draw_pixels(2, 0, 128)
# o.draw_pixels(3, 0, 128)
# o.draw_pixels(7, 0, 128)
# o.draw_pixels(8, 0, 128)
# o.draw_pixels(1, 9, 7)
# o.draw_pixels(9, 9, 7)
# o.draw_pixels(2, 9, 8)
# o.draw_pixels(3, 9, 16)
# o.draw_pixels(4, 9, 33)
# o.draw_pixels(5, 9, 66)
# o.draw_pixels(6, 9, 33)
# o.draw_pixels(7, 9, 16)
# o.draw_pixels(8, 9, 8)
#
# o.draw_pixels(15, 9, 127)
# o.draw_pixels(16, 9, 65)
# o.draw_pixels(17, 9, 65)
# o.draw_pixels(18, 9, 62)
#
# o.draw_pixels(20, 9, 38)
# o.draw_pixels(21, 9, 73)
# o.draw_pixels(22, 9, 73)
# o.draw_pixels(23, 9, 50)
#
# o.draw_pixels(25, 9, 127)
# o.draw_pixels(26, 9, 9)
# o.draw_pixels(27, 9, 9)
# o.draw_pixels(28, 9, 6)
#
# o.draw_pixels(30, 9, 98)
# o.draw_pixels(31, 9, 81)
# o.draw_pixels(32, 9, 73)
# o.draw_pixels(33, 9, 70)
#
# o.draw_pixels(35, 9, 62)
# o.draw_pixels(36, 9, 65)
# o.draw_pixels(37, 9, 65)
# o.draw_pixels(38, 9, 62)
#
# o.draw_pixels(40, 9, 4)
# o.draw_pixels(41, 9, 2+64)
# o.draw_pixels(42, 9, 127)
# o.draw_pixels(43, 9, 64)
#
# o.draw_pixels(40, 9, 4)
# o.draw_pixels(41, 9, 2+64)
# o.draw_pixels(42, 9, 127)
# o.draw_pixels(43, 9, 64)
#
# o.draw_pixels(45, 9, 97)
# o.draw_pixels(46, 9, 25)
# o.draw_pixels(47, 9, 5)
# o.draw_pixels(48, 9, 3)

