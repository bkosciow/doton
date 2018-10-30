Doton
===

Doton project is a control Node for IoT devices. It works on Raspberry Pi and uses ILI9328 or ILI9486 compatible display to show
information in a form of widget/tile.

[Articles](https://koscis.wordpress.com/tag/doton/)

Tiles on 320x480 4" screen:

![screen](https://koscis.files.wordpress.com/2017/05/img_20170524_210024.jpg?w=300)

![screen](https://koscis.files.wordpress.com/2017/05/img_20170506_133912.jpg?w=300)

## Structure

assets - images and fonts

handler - handlers for DHT11, PIR, light sensor, relay

service - Dispatcher, Window Manager, Worker Handler, Openweather, Config

view - NodeOne, Openweather, Clock, Relay

worker - Openweather 

## Configuration

File **config.ini** 

    [lcd]
    ;ili9486  ili9325
    lcd=ili9486
    size=320,480
    rotate=270
    driver=spi
    driver_pins={"CS": 8,"RST": 25,"RS": 24,"LED": ""}
    
    [touch]
    ;xpt2046 ad7843
    driver=xpt2046
    size=480, 320
    rotate=0
    irq=17
    cs=7
    
    [general]
    ;broadcast address
    ip=192.168.1.255
    port=5053
    node_name=control-node-2
    
    [openweather]
    apikey=my-secret-api-key
    cities={"3103402": "Bielsko-Biała"}

## Doton as a service

- Copy file doton.service to /lib/systemd/system/doton.service

- chmod 0644 /lib/systemd/system/doton.service

- adjust drectories and names in file

- start by systemctl start doton

## Attached projects:
- GfxLCD - lib for graphical LCDs on ili9325, ssd1306 and nju6450. Made for Doton project - [repo](https://github.com/bkosciow/gfxlcd) - [Articles](https://koscis.wordpress.com/category/screens/lcd-screens/gfxlcd/)

- Data from NodeOne. [https://koscis.wordpress.com/2017/04/03/node-one-a-multi-purpose-node/](https://koscis.wordpress.com/2017/04/03/node-one-a-multi-purpose-node/)

- message_listener - handler for worker nodes. python implementation - [repo](https://github.com/bkosciow/message_listener) 

- python_message - lib for custom iot:1 protocol. Python implementation - [repo](https://github.com/bkosciow/python_iot-1)   

 
### Credits

Weather icons made by [Freepik](http://www.flaticon.com/authors/freepik) and [Linector](http://www.flaticon.com/authors/linector) from [www.flaticon.com](http://www.flaticon.com)
 
 

