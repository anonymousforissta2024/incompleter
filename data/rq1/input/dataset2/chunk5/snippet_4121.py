#Source: https://stackoverflow.com/questions/51829791/typeerror-unicode-strings-are-not-supported-please-encode-to-bytes-%c3%bf
from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)    