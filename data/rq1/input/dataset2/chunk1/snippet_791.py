#Source: https://stackoverflow.com/questions/50183951/raspberry-pi-python-spi-open-error-filenotfounderror
import spidev
from time import sleep
spi = spidev.SpiDev()
spi.open(1,0)