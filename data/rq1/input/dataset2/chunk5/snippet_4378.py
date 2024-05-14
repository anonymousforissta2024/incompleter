#Source: https://stackoverflow.com/questions/61930815/typeerror-module-object-is-not-callable-apriori
import argparse
import time
import sys
import random
from efficient_apriori import apriori
parser = argparse.ArgumentParser(description="datasets")
parser.add_argument('-f', '--file', 
default="sample.txt",help="http://fimi.uantwerpen.be/data/")
parser.add_argument('-s', '--min_support', default = 0.5,
                help="minimum support, set to 0.5 by default")
parser.add_argument('-c', '--min_confidence', default = 0.5,
                help="minimum confidence, set to 1 by default")
parser.add_argument('-p', '--probability', default = 1,
                help="Probability for randomlized slice")               
args = parser.parse_args()
#memory_data [Brisket_Number][Item_Number]
memory_data = []
data_list = []
def decision(probability):
    return random.random() < float(probability)
#------------------------------------------File Handling------------------------------------------
def file_to_array():
    i = 1
    data_file = open(args.file, "r")
    print("Reading File into Array...\n")
    #if its comment line
    for line in data_file:

        line = line.rstrip()
        line_row = line.split()

        memory_data.append(line_row)
        if (decision(args.probability)):
            data_list.append(tuple(line_row))
        i += 1
    data_file.close()
    #print("Array:",memory_data,"\n")
    #print("Data_list:",data_list)
    print ("Reading complete ",i, " lines in total.")
def main():
    start_time = time.time()
    file_to_array()
    #Apriori()
    itemsets, rules = apriori(data_list, min_support= float(args.min_support),  
min_confidence=float(args.min_confidence))
    #print(itemsets)
    print(rules) 
    print("--- Total run time: %s seconds ---" % (time.time() - start_time))
if __name__ == "__main__":
    main()