#Source: https://stackoverflow.com/questions/59074293/my-script-has-the-answe-typeerror-module-object-is-not-callable-how-i-solve
import time
import serial

ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate = 9600,
    parity=0,
    stopbits=1,
    bytesize=8,
    timeout=1
)

while 1:
    ser.write(b'A')
    x=ser.readline()
    print (x)
    time.sleep(1)