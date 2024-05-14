#Source: https://stackoverflow.com/questions/51700451/python-type-error
STORY = "I was %s at the %s when a %s came along and %s me."

print("Mad Libs has started")

verbing = input("Enter a verb ending in ing: ")

place = input("Enter a place: ")

noun = input("Enter a noun: ")

verb = input("Enter a verb: ")

print (STORY % verbing, place, noun, verb)