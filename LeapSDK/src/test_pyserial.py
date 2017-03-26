# test_pyserial.py


import time, serial

serialConnection = serial.Serial('/dev/ttyUSB1', 9600);

serialConnection.write("Hello world")


