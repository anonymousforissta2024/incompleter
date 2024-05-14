#Source: https://stackoverflow.com/questions/56159725/im-trying-to-use-the-classes-that-i-madevehicle-and-customer-but-i-get-typee
import sys
import csv

vehicle = 0
customers = []

class Vehicle:
    def _init_(self, number, capacity):
        self.number = number
        self.capacity = capacity


class customer:
    def _init_(self, custNo, xCord, yCord, demand, readyT, dueDate, serviceTime):
        self.custNo = custNo
        self.xCord = xCord
        self.yCord = yCord
        self.demand = demand
        self.readyT = readyT
        self.dueDate = dueDate
        self.serviceT = serviceTime


def read():
    global vehicle
    with open('C101 BUENO.csv') as cvs_file:
        cvs_reader = csv.reader(cvs_file, delimiter=';')
        line = 0
        for row in cvs_reader:
            print(line)
            if line == 0 or line == 2:
                line += 1
            elif line == 1:
                vehicle = Vehicle(row[0], row[1])
                line += 1
            else:
                c = customer(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                customers.append(c)
                line += 1

read()