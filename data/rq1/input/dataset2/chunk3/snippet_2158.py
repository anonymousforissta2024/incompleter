#Source: https://stackoverflow.com/questions/72134050/python3-python-can-notifier-typeerror-nonetype-object-is-not-callables
import os
import can

os.system('sudo ip link set can0 up type can bitrate 500000')

bus = can.interface.Bus(channel = 'can0', bustype = 'socketcan')

def parseData(can):
        SingleCanFrame = can.Message

notifier = can.Notifier(bus,[parseData(can)])

while(1):
        continue

os.system('sudo ifconfig can0 down')