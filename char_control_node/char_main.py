from charlcd.buffered import CharLCD
from charlcd.drivers.i2c import I2C
from lcdmanager import manager
from view.readings import Readings
from message_listener.server import Server
from iot_message.message import Message
import sys, time
sys.path.append("../")
from sensors.DHTHandler import DHTHandler
from sensors.PIRHandler import PIRHandler
from sensors.LightHandler import LightHandler

i2c_20x4 = I2C(0x3b, 1)
i2c_20x4.pins = {
    'RS': 6, 'E': 4, 'E2': None, 'DB4': 0, 'DB5': 1, 'DB6': 2, 'DB7': 3
}

lcd = CharLCD(20, 4, i2c_20x4, 0, 0)
lcd.init()
lcd_manager = manager.Manager(lcd)

msg = Message('secondary-node')
view = Readings(lcd_manager)

svr = Server(msg)
svr.add_handler('dht11', DHTHandler(view))
svr.add_handler('pir', PIRHandler(view))
svr.add_handler('light', LightHandler(view))
svr.start()

while True:
    lcd_manager.render()
    lcd_manager.flush()
    time.sleep(1)

svr.join()
