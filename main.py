import RPi.GPIO as GPIO
from gfxlcd.driver.ili9325.gpio import GPIO as ILIGPIO
from gfxlcd.driver.ili9325.ili9325 import ILI9325
import time
GPIO.setmode(GPIO.BCM)


LED = 6
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 1)

lcd_tft = ILI9325(240, 320, ILIGPIO())
lcd_tft.init()

lcd_tft.background_color = (255, 0, 0)
lcd_tft.fill_rect(10, 10, 50, 50)

lcd_tft.background_color = (0, 255, 0)
lcd_tft.fill_rect(230, 50, 190, 10)

lcd_tft.background_color = (0, 0, 255)
lcd_tft.fill_rect(230, 310, 190, 270)

lcd_tft.background_color = (255, 255, 0)
lcd_tft.fill_rect(10, 310, 50, 270)

lcd_tft.draw_circle(120, 160, 100)
lcd_tft.draw_circle(70, 120, 20)
lcd_tft.draw_circle(170, 120, 20)

lcd_tft.background_color = (250, 0, 255)
lcd_tft.draw_arc(120, 160, 70, 20, 160)

lcd_tft.draw_line(120, 150, 115, 180)
lcd_tft.draw_line(120, 150, 125, 180)
lcd_tft.draw_line(115, 180, 125, 180)
