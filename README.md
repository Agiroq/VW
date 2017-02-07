VW_micropython
NodeMCU for a camper 

1- after install esptools to ubuntu:
	
	pip install esptool

2- we need to erase the node device:
	
	esptool.py --port /dev/ttyUSB0 erase_flash

3- flash the mycropython bin rom

	esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 firmware/esp8266-20170108-v1.8.7.bin

5- now we wil install picocom paquet and start a session with:

	picocom /dev/ttyUSB0 -b115200


