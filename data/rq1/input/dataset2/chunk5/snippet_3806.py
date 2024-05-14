#Source: https://stackoverflow.com/questions/38643554/weird-typeerror-when-using-the-datetime-time-module
import os
import datetime as dt
from time import sleep


def  connect():
    print("Connecting...")
    os.system("netsh wlan connect Sushi")

def disconnect():
    print("Disconnecting...")
    os.system("netsh wlan disconnect")

def checkcon():
    attempt= 0
    while os.system("ping google.com") != 0:
        print("Unable to connect. Trying again.")
        connect()
        sleep(attempt)
        attempt = attempt + 1
        if attempt != 0:
            print("Attempt ", str(attempt), " ...")
    print("Connected successfully")


def timeformat (hr, min, sec) : #For setting proper datetime parameters.
    return (str(hr) + ":" + str(min) + ":" + str(sec))

FMT = '%H:%M:%S'
now = timeformat(dt.datetime.now().time().hour, dt.datetime.now().time().minute, dt.datetime.now().time().second)
twoam = '02:00:00'
eightam = '08:00:00'

def tdelta(a, b = now):
        tdel = dt.datetime.strptime(a, FMT) - dt.datetime.strptime(b, FMT)
        return tdel.seconds

twoto8 = tdelta(eightam, twoam)
nowto8 = tdelta(eightam)

def main():
        if  twoto8 >= nowto8:
                connect()
                checkcon()
                print("Your internet has been successfully connected")
                x = tdelta(nowto8)
                sleep(x)
                print("Time's up!")
                disconnect()
                exit()
        else:
                print("Not yet!")
                disconnect()
                x = tdelta(nowto8)
                sleep(str(x))
                main()

main()