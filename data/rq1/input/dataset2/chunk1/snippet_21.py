#Source: https://stackoverflow.com/questions/60288895/lambda-and-typeerror-module-object-is-not-callable
import random
from string import ascii_letters

choice = lambda x: x[int(random()* len(x))]

print(choice("azerty"))