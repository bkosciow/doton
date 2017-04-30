import RPi.GPIO as GPIO
from gfxlcd.driver.ili9325.gpio import GPIO as ILIGPIO
from gfxlcd.driver.ili9325.ili9325 import ILI9325
from view.nodeone_widget import NodeOneWidget
from assets.font import digital_numbers
from message_listener.server import Server
from iot_message.message import Message
from sensors.DHTHandler import DHTHandler
from sensors.PIRHandler import PIRHandler
from sensors.LightHandler import LightHandler
from service.handler_dispatcher import HandlerDispatcher

GPIO.setmode(GPIO.BCM)

msg = Message('control-node')

LED = 6
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 1)

lcd_tft = ILI9325(240, 320, ILIGPIO())
lcd_tft.init()

font = digital_numbers.DigitalNumbers()

WIDGETS = {
    'node-kitchen': NodeOneWidget(0, 0, lcd_tft, font),
    'node-my-room': NodeOneWidget(125, 0, lcd_tft, font),
    #'weather': Widget(0, 108, lcd_tft),
}

WIDGETS['node-kitchen'].colours['background'] = (0, 0, 255)
WIDGETS['node-my-room'].colours['background'] = (0, 255, 255)
for sensor in WIDGETS:
    WIDGETS[sensor].draw_widget()

dispatcher = HandlerDispatcher(WIDGETS)
svr = Server(msg)
svr.add_handler('dht11', DHTHandler(dispatcher))
svr.add_handler('pir', PIRHandler(dispatcher))
svr.add_handler('light', LightHandler(dispatcher))
svr.start()

while True:
    for sensor in WIDGETS:
        WIDGETS[sensor].draw_values()

svr.join()
