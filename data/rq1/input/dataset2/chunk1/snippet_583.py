#Source: https://stackoverflow.com/questions/56898620/typeerror-expected-str-bytes-or-os-pathlike-object-not-none-type
import os
import time
file_path = os.path.join(os.getenv("HOME"), "birth_day_lookup.txt")


def check_birthday():

    lookup_file = open(file_path, 'r')
    today = time.strftime('%d-%B')
    flag = 0
    for entry in lookup_file:
        if today in entry:
            line = entry.split(' ')
            flag = 1
            os.system('notify-send "Today is '+line[1]+' '+line[2]+'\'s Birthday"')
    if flag == 0:
        os.system('notify-send "No birthday for today is listed"')

check_birthday()