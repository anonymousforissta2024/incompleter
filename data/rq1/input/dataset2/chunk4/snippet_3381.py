#Source: https://stackoverflow.com/questions/16353858/type-error-occurred-using-buffer-memoryview
import serial

ser = serial.Serial(
    port='COM5',\
    baudrate=9600,\
    parity=serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
        timeout=0)

MAX_BUF_SIZE = 16
bits = 0

v = memoryview



print("connected to: " + ser.portstr)



while(1):
    for memoryview in ser.read():
        if v[0] == 42:

            if v[-1] == 35:

                print(v[1:-1].tobytes())

        else:
            memoryview = 0
ser.close()