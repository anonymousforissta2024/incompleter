#Source: https://stackoverflow.com/questions/67488541/attributeerror-nonetype-object-has-no-attribute-terminate
import RPi.GPIO as GPIO
from rpi_lcd import LCD
from time import sleep
import time
from multiprocessing import Process


# RPi setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


# Button setup
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Yellow
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # Blue


# LCD setup
lcd = LCD()


# Keypad setup
length = 6
col = [19, 13, 6, 5]
row = [21, 20, 16, 26]

for j in range(4):
    GPIO.setup(col[j], GPIO.OUT)
    GPIO.output(col[j], 1)
for i in range(4):
    GPIO.setup(row[i], GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Password checker
def check_keypad(length):
    col = [19, 13, 6, 5]
    row = [21, 20, 16, 26]

    matrix = [["1", "2", "3", "A"],
              ["4", "5", "6", "B"],
              ["7", "8", "9", "C"],
              ["*", "0", "#", "D"]]
    result = ""

    while True:
        for j in range(4):
            GPIO.output(col[j], 0)

            for i in range(4):
                if GPIO.input(row[i]) == 0:
                    time.sleep(0.02)
                    result = result + matrix[i][j]
                    print(result)
                    while GPIO.input(row[i]) == 0:
                        time.sleep(0.02)

            GPIO.output(col[j], 1)
            if len(result) >= length:
                return result


# Start sequence
def starter():

    global password
    x = 0

    lcd.text("Starting...", 1)
    sleep(5)
    lcd.clear()
    lcd.text("Input a password", 1)

    matrix = [["1", "2", "3", "A"],
              ["4", "5", "6", "B"],
              ["7", "8", "9", "C"],
              ["*", "0", "#", "D"]]
    passwordmaker = ""

    while x != 1:
        lcd.text(passwordmaker, 2)
        for j in range(4):
            GPIO.output(col[j], 0)

            for i in range(4):
                if GPIO.input(row[i]) == 0:
                    time.sleep(0.02)
                    passwordmaker = passwordmaker + matrix[i][j]
                    # print(passwordmaker)  # thingy
                    while GPIO.input(row[i]) == 0:
                        time.sleep(0.02)
            GPIO.output(col[j], 1)
        if len(passwordmaker) == 6:
            lcd.text(passwordmaker, 2)
            password = passwordmaker
            print("Password - " + password)
            x = 1
    sleep(0.5)
    lcd.clear()
    lcd.text("Initiating", 1)
    lcd.text("startup sequence", 2)
    sleep(2)
    lcd.clear()
    sleep(0.5)


# Timer
def timer():

    timeA = 41  # 40 + 1
    while timeA != 0:
        sleep(1)
        timeA = timeA - 1
        lcd.text(str(timeA), 1)
        print(timeA)
    p2.terminate()
    lcd.clear()
    lcd.text("Boom!", 1)


# Code
def code():

    y1 = 3  # Amount of tries
    y2 = 0

    for y in range(3):

        # Password from keypad
        y1str = str(y1)
        text = "( " + y1str + " / 3 )"
        lcd.text(text, 2)
        result = check_keypad(length)
        y1 = y1 - 1

        # Password check
        if result == password:
            y2 = 1
            break

    # Correct password
    if y2 == 1:
        p1.terminate()
        lcd.clear()
        lcd.text("Deactivated", 1)
        sleep(10)

    # Incorrect password
    elif y1 == 0 & y2 == 0:
        p1.terminate()
        lcd.clear()
        lcd.text("Boom!", 1)
        sleep(10)


# Multiprocessing setup
p1 = Process(target=timer)
p2 = Process(target=code)


# Stuff
starter()
p1.start()
p2.start()