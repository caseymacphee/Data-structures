### Python package for the open source RPi-HAUS module ###
### Home Automation User Services ###
###### Configured to be run on Debian-Wheezy BST 2014 armv6l GNU/Linux ######
###########/dev/ttyACM*##########

from serial_port import serial_ports

serial_paths = serial_ports()
LINUX_SERIAL_PATH = '/dev/ttyACM'

serial_connections = []

