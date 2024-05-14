#Source: https://stackoverflow.com/questions/47298943/made-a-program-in-python-but-get-typeerror-method-object-is-not-subscriptable
import pyowm
import datetime
import csv

W = pyowm.OWM("****************************")
myHouse = W.weather_at_place("St. albert,Canada")
myWeather = myHouse.get_weather()
wind = myWeather.get_wind()
windspeed = wind["speed"]
windangle = wind["deg"]
humidity = myWeather.get_humidity()
temperature = myWeather.get_temperature("celsius")
high = temperature["temp_max"]
low = temperature["temp_min"]
current = temperature["temp"]
date = datetime.datetime.now().strftime("%D")
time = datetime.datetime.now().strftime("%H")

done=0

while True:
    if datetime.datetime.now().strftime("%S") == "00" and done == 0:
        done=1
        csvfile = open("weatherCSV.csv", "w")
        writeCSV = csv.writer(csvfile, delimiter=",")

        myWeather = myHouse.get_weather()
        wind = myWeather.get_wind
        windspeed = wind["speed"]
        windangle = wind["deg"]
        humidity = myWeather.get_humidity()
        temperature = myWeather.get_temperature("celsius")
        high = temperature["temp_max"]
        low = temperature["temp_min"]
        current = temperature["temp"]
        date = datetime.datetime.now().strftime("%D")
        time = datetime.datetime.now().strftime("%H")


        writeCSV.writerow([current,high,low,windspeed,windangle,humidity,date,time])
        csvfile.close()
        print("Added to file")

    if datetime.datetime.now().strftime("%S") == "30" and done == 1:
        done=0