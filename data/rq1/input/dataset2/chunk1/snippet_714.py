#Source: https://stackoverflow.com/questions/35642855/python3-pyserial-typeerror-unicode-strings-are-not-supported-please-encode-to
import serial, time
import tkinter
import os

def serialcmdw():
    os.system('clear')
    serialcmd = input("serial command: ")
    ser.write (serialcmd)

serialcmdw()

ser = serial.Serial()
os.system('clear')
ser.port = "/dev/cu.usbmodem4321"
ser.baudrate = 9600
ser.open()
time.sleep(1)
serialcmdw()