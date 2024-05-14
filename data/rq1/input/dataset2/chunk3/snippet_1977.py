#Source: https://stackoverflow.com/questions/63683032/attributeerror-sqlite3-connection-object-attribute-execute-is-read-only-p
import os, sys
import sqlite3
from sqlite3 import Error

connection = None
try:
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    print("Connection to SQLite DB successful")
except Error as e:
    print(f"The error '{e}' occurred")

cursor.execute("""CREATE TABLE IF NOT EXISTS Tickets ( 
    id INT,
    indexNumber INT,
    movieNumber INT,
    screeningHall VARCHAR(30),
    movieName VARCHAR(30),
    screeningDate VARCHAR(30),
    screeningTime VARCHAR(30),
    ticketRow INT,
    ticketCol INT,
    ticketType VARCHAR(30),
    ticketPrice VARCHAR(30))"""
)
idNum = 0
tempInfoDict = {'indexNumber': 0, 'movieNumber': 1, 'hall': 'Hall 1', 'name': 'Terminator', 'date': '2020-09-01', 'time': '10:40', 'row': 1, 'col': 0}

connection.execute = ("INSERT INTO Tickets (id, indexNumber, movieNumber, screeningHall, movieName, screeningDate, screeningTime, ticketRow, ticketCol, ticketType, ticketPrice) values(?,?,?,?,?,?,?,?,?,?,?)",
                                            (idNum, tempInfoDict['indexNumber'], tempInfoDict['movieNumber'], tempInfoDict['hall'], tempInfoDict['name'],
                                            tempInfoDict['date'], tempInfoDict['time'], tempInfoDict['row'], tempInfoDict['col'], 'Basic', '$20'))

connection.commit()
connection.close()