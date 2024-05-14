#Source: https://stackoverflow.com/questions/69774299/typeerror-float-argument-must-be-a-string-or-a-number-not-datetime-timedelt
import matplotlib.pyplot as plt
import numpy as np
import serial as ser
import time
import datetime
import mysql.connector


my_connect = mysql.connector.connect(host="localhost", user="Kennedy", passwd="Kennerdol05071994", database="ecg_db", auth_plugin="mysql_native_password")
mycursor = my_connect.cursor()

voltage_container = []
time_container = []


def fetch_voltage():
    pat_id = 1
    query = "SELECT voltage, time FROM ecg_data_tbl where patient_id = 1 "
    mycursor.execute(query)
    result = mycursor .fetchall()
    voltage, time = list(zip(*result))
    for volts in voltage:
        voltage_container.append(volts)
        voltage_data = np.array(voltage_container)
    for tim in time:
        time_container.append(tim)
        time_data = np.array(time_container)
    plt.plot(time_data, voltage_data)
    

fetch_voltage()