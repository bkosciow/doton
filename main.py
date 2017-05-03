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
from service.window_manager import WindowManager
from service.config import Config
GPIO.setmode(GPIO.BCM)

config = Config()

msg = Message(config.get('node_name'))

LED = 6
GPIO.setup(LED, GPIO.OUT)
GPIO.output(LED, 1)

lcd_tft = ILI9325(240, 320, ILIGPIO())
lcd_tft.init()
window_manager = WindowManager(lcd_tft)

FONTS = {
    '24x42': numbers_24x42.Numbers(),
    '15x28': numbers_15x28.Numbers()
}

window_manager.add_widget('node-kitchen', [(0, 0)], NodeOneWidget(FONTS['24x42']))
window_manager.add_widget('node-my-room', [(1, 0)], NodeOneWidget(FONTS['24x42']))
window_manager.add_widget('openweather', [(0, 1), (1, 1)], OpenweatherWidget(FONTS))
window_manager.set_widget_color('node-my-room', 'background', (0, 255, 255))
window_manager.start()

dispatcher = HandlerDispatcher(window_manager.get_widgets())
svr = Server(msg)
svr.add_handler('dht11', DHTHandler(dispatcher))
svr.add_handler('pir', PIRHandler(dispatcher))
svr.add_handler('light', LightHandler(dispatcher))
svr.start()

workerHandler = WorkerHandler()
workerHandler.add('openweather', OpenweatherWorker(config.get('openweather_apikey'), window_manager.get_widget('openweather')), 5)
workerHandler.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("closing...")
except:
    raise
finally:
    workerHandler.stop()
    window_manager.stop()
    window_manager.join()
    workerHandler.join()
    svr.join()
