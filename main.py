import RPi.GPIO as GPIO
import time
import socket
from view.nodeone_widget import NodeOneWidget
from view.openweather_widget import OpenweatherWidget
from view.relay_widget import RelayWidget
from assets.font import numbers_24x42
from assets.font import numbers_15x28
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
GPIO.setmode(GPIO.BCM)

config = Config()

msg = Message(config.get('node_name'))

broadcast_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
broadcast_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
address = (config.get('ip', '<broadcast>'), int(config.get('port')))

window_manager = WindowManager(config)
window_manager.drop_out_of_bounds = True
FONTS = {
    '24x42': numbers_24x42.Numbers(),
    '15x28': numbers_15x28.Numbers()
}

window_manager.add_widget('node-kitchen', [(0, 0)], NodeOneWidget(FONTS['24x42']))
window_manager.add_widget('openweather', [(0, 1), (1, 1), (2, 1), (3, 1), (4, 1)], OpenweatherWidget([0, 1, 2], FONTS))
window_manager.add_widget(
    'my-room-light', [(0, 2), (1, 2)],
    RelayWidget(msg, 'my-room-light', broadcast_socket, address, 2)
)
window_manager.add_widget('node-my-room-2', [(1, 0)], NodeOneWidget(FONTS['24x42']))

window_manager.add_widget('node-kitchen-2', [(0, 1)], window_manager.get_widget('node-kitchen'), 1)
window_manager.add_widget('node-my-room', [(1, 2)], NodeOneWidget(FONTS['24x42']), 1)

window_manager.add_widget('more-weather', [(0, 2), (1, 2)], window_manager.get_widget('openweather'), 2)

window_manager.set_widget_color('node-my-room', 'background', (0, 255, 255))
window_manager.set_widget_color('node-my-room-2', 'background', (0, 255, 255))

window_manager.start()

dispatcher = HandlerDispatcher({
    'node-kitchen': [window_manager.get_widget('node-kitchen')],
    'node-my-room': [window_manager.get_widget('node-my-room'), window_manager.get_widget('node-my-room-2')],
    'openweather': [window_manager.get_widget('openweather')],
    'my-room-light': [window_manager.get_widget('my-room-light')]
})
svr = Server(msg)
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
