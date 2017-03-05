import RPi.GPIO as GPIO
from screen import TFT
GPIO.setmode(GPIO.BCM)


LED = 6
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 1)


s = TFT()
s.init()

for i in range(0, 11):
    s.draw_pixel(100 + i, 100)
    s.draw_pixel(100 + i, 110)
    s.draw_pixel(100, 100 + i)
    s.draw_pixel(110, 100 + i)

    s.draw_pixel(160 + i, 100)
