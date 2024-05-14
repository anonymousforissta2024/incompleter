#Source: https://stackoverflow.com/questions/59362975/dont-understand-this-timed-while-loop-attribute-error
import math
from datetime import datetime
import time


test_num = 1
largest_loop = 0
delay = 60 * 10
end_time = time.time() + delay


def even_number(value):
    if value == 2:
        return True


def divide_five(value):
    if value == 5:
        return True


def is_square(value):
    if math.sqrt(value).is_integer():
        return False


def multiple_of(value):
    if value == 2:
        return True


def is_happy():
    global check
    if check == 1:
        return True


while time.time() <= end_time:
    test_num += 1
    check = test_num
    now = datetime.now()
    loop_counter = 0
    record_loop = 6
    date = now.strftime("%m/%d/%Y")
    time = now.strftime("%H:%M:%S")
    if even_number(test_num) == True:
        if divide_five(test_num) == True:
            if is_square(test_num) == True:                
                for _ in range(record_loop + 4):
                    loop_counter += 1                            
                    if is_happy() == True:
                        if multiple_of(test_num) == True:
                            #print(test_num)
                            record_loop = loop_counter
                            break
                        else:
                            pass
                else:
                    pass
            else:
                pass
        else:
            pass        
    else:
        pass