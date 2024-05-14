#Source: https://stackoverflow.com/questions/66701388/typeerror-unsupported-operand-types-for-float-and-int
import math
phi = math.sqrt(5) / 2
pi = (802 * phi - 801) / (602 * phi - 601)
pi = round(pi ^ 4)
print("Pi is equivalent to", pi)