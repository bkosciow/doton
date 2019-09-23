import RPi.GPIO as GPIO
import time
import socket
from view.nodeone_widget import NodeOneWidget
from view.openweather_widget import OpenweatherWidget
from view.relay_widget import RelayWidget
from view.clock_widget import ClockWidget
from assets.font import numbers_24x42
from assets.font import numbers_15x28
from assets.font import numbers_15x28_red
from assets.font import numbers_15x28_blue
from message_listener.server import Server
from iot_message.message import Message
from handler.DHTHandler import DHTHandler
from handler.PIRHandler import PIRHandler
from handler.LightHandler import LightHandler
from handler.RelayHandler import RelayHandler
from service.handler_dispatcher import HandlerDispatcher
from service.worker_handler import Handler as WorkerHandler
from worker.openweather import OpenweatherWorker
from service.window_manager import WindowManager
from service.config import Config
from iot_message.cryptor.base64 import Cryptor as B64
from iot_message.cryptor.plain import Cryptor as Plain
from iot_message.cryptor.aes_sha1 import Cryptor as AES

GPIO.setmode(GPIO.BCM)

config = Config()

Message.node_name = config.get('node_name')
Message.add_encoder(B64())
Message.add_encoder(Plain())
Message.add_encoder(AES(
    'abcdef2345678901', '2345678901abcdef', '0123456789abcdef', 'mypassphrase'
))

Message.add_decoder(B64())
Message.add_decoder(AES(
    'abcdef2345678901', '2345678901abcdef', '0123456789abcdef', 'mypassphrase'
))

broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
address = (config.get('ip', '<broadcast>'), int(config.get('port')))

window_manager = WindowManager(config)
window_manager.drop_out_of_bounds = True
FONTS = {
    '24x42': numbers_24x42.Numbers(),
    '15x28': numbers_15x28.Numbers(),
    '15x28_red': numbers_15x28_red.Numbers(),
    '15x28_blue': numbers_15x28_blue.Numbers(),
}

window_manager.add_widget('clock', [(3, 2)], ClockWidget(FONTS['15x28']))
window_manager.add_widget('openweather', [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], OpenweatherWidget([0, 1, 2], FONTS))

window_manager.add_widget('my-room-light', [(0, 2)], RelayWidget('node-living', broadcast_socket, address, 1))
window_manager.add_widget('north-room-light', [(1, 2)], RelayWidget('node-north', broadcast_socket, address, 1))

#
window_manager.add_widget('node-kitchen', [(0, 0)], NodeOneWidget(FONTS['24x42']))
window_manager.add_widget('node-living', [(1, 0)], NodeOneWidget(FONTS['24x42']))
window_manager.add_widget('node-north', [(2, 0)], NodeOneWidget(FONTS['24x42']))

window_manager.set_widget_color('node-living', 'background', (0, 255, 255))
window_manager.set_widget_color('node-north', 'background', (128, 128, 255))

window_manager.start()

dispatcher = HandlerDispatcher({
    'node-kitchen': [window_manager.get_widget('node-kitchen')],
    'node-living': [window_manager.get_widget('node-living'), window_manager.get_widget('my-room-light')],
    'node-north': [window_manager.get_widget('node-north'), window_manager.get_widget('north-room-light')],
    'openweather': [window_manager.get_widget('openweather')],
})
svr = Server()
svr.add_handler('dht11', DHTHandler(dispatcher))
svr.add_handler('pir', PIRHandler(dispatcher))
svr.add_handler('light', LightHandler(dispatcher))
svr.add_handler('relay', RelayHandler(dispatcher))
svr.start()

workerHandler = WorkerHandler()
workerHandler.add('openweather', OpenweatherWorker(config.get_section('openweather'), window_manager.get_widget('openweather')), 5)
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
