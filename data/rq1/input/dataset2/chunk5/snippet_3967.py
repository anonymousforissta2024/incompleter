#Source: https://stackoverflow.com/questions/57599957/attributeerror-serialbus-object-has-no-attribute-can
from can.interfaces import serial

import random
import time
import datetime
import matplotlib.pyplot as plt

ser= can.interfaces.serial.serial_can.SerialBus('COM5',115200,timeout=None,rtscts=0)

for i in range(100) :
    s= ser.can.interfaces.serial.SerialBus._recv_internal(timeout=None)
    print(s)