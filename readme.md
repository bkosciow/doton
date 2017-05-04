One repo to rule them all. Doton project for Get Noticed! / Daj się poznać.
===

Doton project is a control Node for IoT devices. It works on Raspberry Pi and uses ILI9328 compatible display to show
information in a form of widget/tile.

Improved weather widget:

![screen](https://koscis.files.wordpress.com/2017/05/img_20170504_134436.jpg?w=400)

Weather and Node One widget:

![screen](https://koscis.files.wordpress.com/2017/05/img_20170502_143440.jpg?w=400)

A widget to display data from the [Node One](https://koscis.wordpress.com/2017/04/03/node-one-a-multi-purpose-node/).

![screen](https://koscis.files.wordpress.com/2017/04/img_20170430_152606.jpg?w=400)


## module char_control_node
Displays data from Node One on HD44780. [https://koscis.wordpress.com/2017/04/03/node-one-a-multi-purpose-node/](https://koscis.wordpress.com/2017/04/03/node-one-a-multi-purpose-node/)

![nodeone](https://koscis.files.wordpress.com/2017/04/sensor_lcd.jpg?w=620)

## Structure

assets - images and fonts

handler - handlers for DHT11, PIR and light sensor

service - Dispatcher, Window Manager, Worker Handler, Openweather, Config

view - NodeOne, Openweather

worker - Openweather 


## Attached projects:
- GfxLCD - lib for graphical LCDs on ili9325, ssd1306 and nju6450. Made for Doton project - [repo](https://github.com/bkosciow/gfxlcd) - [Articles](https://koscis.wordpress.com/category/screens/lcd-screens/gfxlcd/)

![heart](https://koscis.files.wordpress.com/2017/03/img_20170322_205114.jpg?w=200)
![both](https://koscis.files.wordpress.com/2017/04/img_20170420_215316.jpg?w=620)

![main](https://koscis.files.wordpress.com/2017/04/img_20170423_155356.jpg?w=300)

- CharLCD - lib for char lcds on hd44780 - [repo](https://bitbucket.org/kosci/charlcd) - [Articles](https://koscis.wordpress.com/category/charlcd/)

- message_listener - handler for worker nodes. python implementation - [repo](https://github.com/bkosciow/message_listener) 

- python_message - lib for custom iot:1 protocol. Python implementation - [repo](https://github.com/bkosciow/python_iot-1)   

- nodemcu_boilerplate - LUA scripts for NodeMCU that takes care of WiFi and gives few libraries (for char lcds, relay, 18b20). 
It implement message_listener, handlers and iot:1    
[repo](https://github.com/bkosciow/nodemcu_boilerplate) - [Articles](https://koscis.wordpress.com/tag/nodemcu-boilerplate/)

- esp_remote_lcd - Remote LCD = NodeMCU + HD44780 accessible via WiFi. Uses [NodeMCU boilerplate](https://github.com/bkosciow/nodemcu_boilerplate) - 
[repo](https://github.com/bkosciow/esp_remote_lcd) - [Articles](https://koscis.wordpress.com/tag/proxy-lcd/)

- proxy_lcd - Desktop app for managing remote lcds.  opens port 5054 and stream content to lcds. [repo](https://github.com/bkosciow/proxy_lcd) - [Articles](https://koscis.wordpress.com/tag/proxy-lcd/)

- ProxyLCDBundle - Symfony3 bundle that extends dump() and transmit content to proxy_lcd and to remote lcd
[repo](https://github.com/bkosciow/ProxyLCDBundle) - [Articles](https://koscis.wordpress.com/tag/proxy-lcd/)

- lcdmanager - simple window manager for CharLCD module [repo](https://bitbucket.org/kosci/lcdmanager) - [Articles](https://koscis.wordpress.com/category/screens/lcd-screens/lcd-manager/)
 
### Credits

Weather icons made by [Freepik](http://www.flaticon.com/authors/freepik) and [Linector](http://www.flaticon.com/authors/linector) from [www.flaticon.com](http://www.flaticon.com)
 
 

