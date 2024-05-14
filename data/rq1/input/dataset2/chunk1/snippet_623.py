#Source: https://stackoverflow.com/questions/20484195/typeerror-range-object-does-not-support-item-assignment
import random

emails = {
    "x": "[REDACTED]@hotmail.com",
    "x2": "[REDACTED]@hotmail.com",
    "x3": "[REDACTED]@hotmail.com"
}

people = emails.keys()

#generate a number for everyone
allocations = range(len(people))
random.shuffle(allocations)