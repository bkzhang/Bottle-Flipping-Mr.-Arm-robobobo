# test_pyserial.py


import time, serial

serialConnection = serial.Serial('/dev/ttyUSB1', 9600);

vals = [1, 123, 100]
string = chr(vals[0]) + chr(vals[1]) + chr(vals[2])

serialConnection.write(string)


