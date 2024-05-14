#Source: https://stackoverflow.com/questions/47389828/attribute-error-when-using-popen
import os
import RPi.GPIO as GPIO
import time
import sys
import subprocess

os.system('raspistill -o image.jpg -w 1280 -h 1024')
x = os.system('cp image.jpg /home/pi/face_recognition/face_recognition/unknown/unknown.jpg')
print(x)

process = subprocess.Popen('python3 cli.py known unknown | cut -d "," -f2', shell=True)
process.wait()
output = process.check_output()
print(output)

if output == b'unknown_person\n':
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    print("Red LED on")
    GPIO.output(18,GPIO.HIGH)
    time.sleep(3)
    print("Red LED off")
    GPIO.output(18,GPIO.LOW)
else:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(17,GPIO.OUT)
    print("Green LED on")
    GPIO.output(17,GPIO.HIGH)
    time.sleep(3)
    print("Green LED off")
    GPIO.output(17,GPIO.LOW)