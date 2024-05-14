#Source: https://stackoverflow.com/questions/73888842/error-on-code-typeerror-not-supported-between-instances-of-nonetype-and
import RPi.GPIO as GPIO
import Adafruit_DHT
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)


SENSOR_DHT = Adafruit_DHT.DHT22
PIN_DHT = 17
PIN_LED = 22


while True:
    humedad, temperatura = Adafruit_DHT.read(SENSOR_DHT, PIN_DHT)
    if humedad is not None and temperatura is not None:
        print("Temp={0:0.1f}%C Hum={1:0.1f}%".format(temperatura, humedad))
        print(temperatura)
    else:
        print("Falla en la lectura. Revisar el circuito");
    time.sleep(0.5);
    

    if temperatura > 28:
        GPIO.output(22,1)
    else:
        GPIO.output(22,0)