#Source: https://stackoverflow.com/questions/56915197/attributeerror-str-object-has-no-attribute-sleep
#!/usr/bin/python3

import os
import json
import datetime
import cgi
import time

def save(number_input, current_time):
    i = 0
    while os.path.exists("datei/datei{}.txt".format(i)):
        i += 1

    datei = {
        "input": number_input,
        "zeit": current_time
    }

    with open("datei/datei{}.txt".format(i), "w+") as file:
        json.dump(datei, file)

form = cgi.FieldStorage(encoding="utf-8")

number = form.getvalue("first")
time = datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")

save(number, time)

print("<p>Sie haben {} in einer .txt Datei gespeichert!              </p>".format(number))                              
time.sleep(4)
print("Location: main.py")
print()