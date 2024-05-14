#Source: https://stackoverflow.com/questions/21149842/nameerror-name-last-days-is-not-defined-trying-to-divide
import math

amount = input("Enter amount of medicine left: ")
dose = input("Enter dose per day: ")

def convertString(str):
    try:
        returnValue = int(str)
    except ValueError:
        returnValue = float(str)
    return returnValue

def count_days(amount, dose):
    last_days = amount / dose
    return last_days

print("Your medicine will run out in ",last_days," days.")