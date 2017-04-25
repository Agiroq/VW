# VW_micropython
#### Personal project in development
### NodeMCU for a camper
- [] heater control everspacher H2L.    
- [] gas detection for freezer.    

1- Install esptools to ubuntu:

	pip install esptool

2- It is better to erase the node device:

	esptool.py --port /dev/ttyUSB0 erase_flash

3- And flash the mycropython bin rom

	esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 firmware/esp8266-20170108-v1.8.7.bin

5- Now we wil install picocom paquet from repositories and start a session with to comunicate with module:

	picocom /dev/ttyUSB0 -b115200

6- per copiar fitxers al nostre nodeMCU farem servir ampy de adafruit
l'instal.lem amb "sudo pip3 install adafruit-ampy" i hi desem els fitxers a l'arrel amb:

	ampy --port /dev/ttyUSB0 put main.py
