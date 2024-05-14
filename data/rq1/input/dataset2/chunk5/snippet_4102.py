#Source: https://stackoverflow.com/questions/61632870/raspberrypi-typeerror-unsupported-format-string-passed-to-nonetype-format
import sys
import Adafruit_DHT
import time

while True:

    humidity, temperature = Adafruit_DHT.read_retry(11, 4)

    print( 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
   # print()
time.sleep(1)