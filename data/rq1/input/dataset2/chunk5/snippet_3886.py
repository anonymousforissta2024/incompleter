#Source: https://stackoverflow.com/questions/28926281/filenotfounderror-winerror-2-the-system-cannot-find-the-file-specified
import time
import os

#Acquires current time
from datetime import datetime
current_time = str(datetime.now())
current_time = (time.strftime('%Y-%m-%d %H-%M'))
print(current_time)

OUTPUT_FILE = ("{}.txt".format(current_time))

NEW_DIRS =[]

while 1:
#Acquires list of dirs and the creation date attribute associated to them 
    for dir in os.listdir("S:\\"):
        dir = os.path.join("S:\\", dir)
        if os.path.isdir(dir):

            try:
                seconds = os.path.getctime(dir)
                datecreated = (time.strftime('%Y-%m-%d %H:%M', time.localtime(seconds)))


            except (FileNotFoundError, IOError,AttributeError):
                print("{} Missing!").format(dir)


            close_time = "23-59"

            DATE_TIME = str(datetime.now())
            DATE_TIME = (time.strftime('%H-%M'))

            if DATE_TIME == close_time:
                    quit()

            elif dir not in NEW_DIRS and datecreated > current_time:
                with open(OUTPUT_FILE,"a") as c:
                    c.write("{}\n".format(dir))
                    NEW_DIRS.append(dir)
                    print ("{} added to array".format(dir))