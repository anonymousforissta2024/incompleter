#Source: https://stackoverflow.com/questions/72999836/micropython-application-throws-attributeerror-for-very-basic-use-of-re-split-wit
from machine import Pin, SPI, UART
from array import array
import sys, re, time, math, framebuf

sys.path.append("C:/Source/Pico/SSD1322_SPI_4W")
print(sys.path)
import ssd1322

print("Test print")
s1="123\t123\t123"
s2 = re.split(r'\t', s1)
print(s2)