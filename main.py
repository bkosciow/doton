import RPi.GPIO as GPIO
from screen import TFT
import time
GPIO.setmode(GPIO.BCM)


LED = 6
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 1)

s = TFT()
s.init()

s.bcolor = {'R': 255, 'G': 0, 'B': 0}
s.fill_rect(10, 10, 50, 50)

s.bcolor = {'R': 0, 'G': 255, 'B': 0}
s.fill_rect(230, 50, 190, 10)

s.bcolor = {'R': 0, 'G': 0, 'B': 255}
s.fill_rect(230, 310, 190, 270)

s.bcolor = {'R': 255, 'G': 255, 'B': 0}
s.fill_rect(10, 310, 50, 270)

s.draw_circle(120, 160, 100)
s.draw_circle(70, 120, 20)
s.draw_circle(170, 120, 20)

s.bcolor = {'R': 250, 'G': 0, 'B': 255}
s.draw_arc(120, 160, 70, 20, 160)

s.draw_line(120, 150, 115, 180)
s.draw_line(120, 150, 125, 180)
s.draw_line(115, 180, 125, 180)

# for i in range(0, 11):
#     s.draw_pixel(100 + i, 100)
#     s.draw_pixel(160 + i, 100)
#
#
# s.color = {'R': 128, 'G': 128, 'B': 128}
#
# for i in range(1, 11):
#     s.draw_line(0, i * 30, 239, i * 30)
#
# for i in range(1, 9):
#     s.draw_line(i * 30, 0, i * 30, 319)
#
#
# s.color = {'R': 255, 'G': 0, 'B': 0}
# s.draw_line(60, 60, 47, 202)
# s.color = {'R': 0, 'G': 255, 'B': 0}
# s.draw_line(60, 60, 73, 202)
#
# s.color = {'R': 0, 'G': 0, 'B': 255}
# s.draw_line(180, 240, 167, 88)
# s.color = {'R': 255, 'G': 255, 'B': 0}
# s.draw_line(180, 240, 193, 88)
#
#
# s.color = {'R': 255, 'G': 0, 'B': 0}
# s.draw_line(60, 50, 150, 57)
# s.color = {'R': 0, 'G': 255, 'B': 0}
# s.draw_line(150, 43, 60, 50)
#
# s.color = {'R': 0, 'G': 0, 'B': 255}
# s.draw_line(60, 270, 182, 241)
# s.color = {'R': 255, 'G': 255, 'B': 0}
# s.draw_line(182, 292, 60, 270)
#
# s.color = {'R': 255, 'G': 255, 'B': 255}
# s.draw_rect(30,30, 210, 290)