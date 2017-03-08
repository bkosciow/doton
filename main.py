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
    s.draw_pixel(160 + i, 100)


s.color = {'R': 200, 'G': 200, 'B': 200}

for i in range(1, 11):
    s.draw_line(0, i * 30, 239, i * 30)

for i in range(1, 9):
    s.draw_line(i * 30, 0, i * 30, 319)


s.color = {'R': 255, 'G': 0, 'B': 0}
s.draw_line(60, 60, 47, 202)
s.color = {'R': 0, 'G': 255, 'B': 0}
s.draw_line(60, 60, 73, 202)

s.color = {'R': 0, 'G': 0, 'B': 255}
s.draw_line(180, 240, 167, 88)
s.color = {'R': 255, 'G': 255, 'B': 0}
s.draw_line(180, 240, 193, 88)


s.color = {'R': 255, 'G': 0, 'B': 0}
s.draw_line(60, 50, 150, 57)
s.color = {'R': 0, 'G': 255, 'B': 0}
s.draw_line(150, 43, 60, 50)

s.color = {'R': 0, 'G': 0, 'B': 255}
s.draw_line(60, 270, 182, 241)
s.color = {'R': 255, 'G': 255, 'B': 0}
s.draw_line(182, 292, 60, 270)

s.color = {'R': 0, 'G': 255, 'B': 255}
s.draw_rect(30,30, 210, 290)