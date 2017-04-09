One repo to rule them all. Doton project for Get Noticed! / Daj się poznać.
===
## module char_control_node
Displays data from Node One on HD44780. [https://koscis.wordpress.com/2017/04/03/node-one-a-multi-purpose-node/](https://koscis.wordpress.com/2017/04/03/node-one-a-multi-purpose-node/)

![nodeone](https://koscis.files.wordpress.com/2017/04/sensor_lcd.jpg?w=620)

## Files

### main.py + screen.py - proof of concept, TFT 2.4"
![smile](https://koscis.files.wordpress.com/2017/03/img_20170315_214646.jpg?w=320)

### nju.py - poc for NJU6450

![heart](https://koscis.files.wordpress.com/2017/03/img_20170318_130058.jpg?w=300&h=131)


## Attached projects:
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
 
 

