#Source: https://stackoverflow.com/questions/65224915/why-am-i-unable-to-use-list-object-syntax-and-am-met-with-attributeerror-when-r
import csv

class Volunteer:
 def __init__(self,name,coin_type,weight_of_bag,true_count):
    self.name = name
    self.coin_type = coin_type        #a function allowing me to class the data
    self.weight_of_bag = weight_of_bag
    self.TrueCount = true_count

with open("CoinCount.txt","r+") as csvfile:  #opens file as CSV *IMPORTANT*
    volunteers = []
    for line in csvfile:
        volunteers.append(Volunteer(*line.strip().split(',')))