import RPi.GPIO as GPIO
import time
from gfxlcd.driver.ili9325.gpio import GPIO as ILIGPIO
from gfxlcd.driver.ili9325.ili9325 import ILI9325
from view.nodeone_widget import NodeOneWidget
from view.openweather_widget import OpenweatherWidget
from assets.font import numbers_24x42
from assets.font import numbers_15x28
from message_listener.server import Server
from iot_message.message import Message
from handler.DHTHandler import DHTHandler
from handler.PIRHandler import PIRHandler
from handler.LightHandler import LightHandler
from service.handler_dispatcher import HandlerDispatcher
from service.worker_handler import Handler as WorkerHandler
from worker.openweather import OpenweatherWorker

GPIO.setmode(GPIO.BCM)

msg = Message('control-node')

LED = 6
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 1)

lcd_tft = ILI9325(240, 320, ILIGPIO())
lcd_tft.init()

FONTS = {
    '24x42': numbers_24x42.Numbers(),
    '15x28': numbers_15x28.Numbers()
}

WIDGETS = {
    'node-kitchen': NodeOneWidget(0, 0, lcd_tft, FONTS['24x42']),
    'node-my-room': NodeOneWidget(124, 0, lcd_tft, FONTS['24x42']),
    'openweather': OpenweatherWidget(
        ((0, 108), (124, 108)),
        lcd_tft,
        FONTS
    )
}

# WIDGETS['node-kitchen'].colours['background'] = (0, 0, 255)
WIDGETS['node-my-room'].colours['background'] = (0, 255, 255)

for sensor in WIDGETS:
    WIDGETS[sensor].draw_widget()

dispatcher = HandlerDispatcher(WIDGETS)
svr = Server(msg)
svr.add_handler('dht11', DHTHandler(dispatcher))
svr.add_handler('pir', PIRHandler(dispatcher))
svr.add_handler('light', LightHandler(dispatcher))
svr.start()

workerHandler = WorkerHandler()
workerHandler.add('openweather', OpenweatherWorker('f84b3bdc96fa56451de722087658bffb', WIDGETS['openweather']), 5)
workerHandler.start()

try:
    while True:
        for sensor in WIDGETS:
            WIDGETS[sensor].draw_values()
        time.sleep(0.025)
except KeyboardInterrupt:
    print("closing...")
except:
    raise
finally:
    workerHandler.stop()

workerHandler.join()
svr.join()
