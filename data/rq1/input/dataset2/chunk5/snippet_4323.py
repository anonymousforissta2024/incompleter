#Source: https://stackoverflow.com/questions/66919883/python-functions-in-classes-nameerror
#Import library
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

#Automatically creates a dataframe don't need pd.DataFrame
data = pd.read_csv("/Users/tianachargin/Desktop/PythonSG/STAT 4490/WidgeOne_CSV.csv")
#print out dataset
print(data)

class Graphs: 
#Constructor with parameters
    #Self isn't a pass by value parameter but it allows you to reference
    def __init__(self, quantVar1, quantVar2, qualVar1, qualVar2):   
        self.A = quantVar1   #First quantitative variable           
        self.B = quantVar2   #Second quantitative variable
        self.C = qualVar1    #First qualitative variable
        self.D = qualVar2    #Second qualitative variable 
        
#Function that calculates bin width for the histogram 
    def bin_width(variable):
        #Import libaray
        import math
        
        #Create variable to create array for bins
        #Find min of column
        min = data[variable].min()
        #Find max of column
        max = data[variable].max()
        #Find the the count of rows (number of data/size/n)
        index = data.index
        number_of_rows = len(index) 
        #Calculate number of bins and round up
        num_of_bins = (math.ceil(math.sqrt(number_of_rows)))
        #Calculate bin width (max - min)/# of bins
        bin_width = ((max - min)/num_of_bins)
        #Round bin width to one decimal place
        increment_bin = round(bin_width, 1)
        #Start bin 
        start_bin = (min - increment_bin)
        #End bin
        end_bin = (max + increment_bin)
        
        return start_bin, end_bin, increment_bin
        
#Histogram Function 
    def histogram(self):
        #Import libraries
        import math
        import numpy as np
        import matplotlib.pyplot as plt
        
        #Create variable that we call the function to calculate the bin width
        bin = bin_width(self.A) 
         
        #Start at value = bin[0], Stop at value = bin[1], Increment by value of bin[2]
        bins = np.array(np.arange(start = bin[0], stop = bin[1], step = bin[2]))
        #Histogram function
        plt.hist(data[self.A], bins, label = self.A, color = "red")
        #x-axis label
        plt.xlabel(self.A, fontsize = 16)  
        #y-axis lable
        plt.ylabel("Frequency of " + self.A, fontsize = 16)
        #Title of graph
        plt.title("Histogram of " + self.A, loc = 'center')
        plt.show()
        return


#Stacked Histogram Function  
    def stacked_histogram(self):
        #Import libraries
        import numpy as np
        from matplotlib import pyplot as plt
        
        #Create combonations of the values for the two options
        data[self.C + "-" + self.D] = data[self.C] + " " + data[self.D] 
        combos = np.unique(data[self.C + "-" + self.D])
        #Create variable that we call the function to calculate the bin width
        bin = bin_width(self.A)
        #Start at value = bin[0], Stop at value = bin[1], Increment by value of bin[2]
        bins = np.array(np.arange(start = bin[0], stop = bin[1], step = bin[2]))
        
        #Create histogram
        for i in range(len(combos)):
           plt.hist(data[data[self.C + "-" + self.D].isin(combos[i:(len(combos))])][self.A], bins, label = combos[i:(len(combos))])
        #x-axis label
        plt.xlabel(self.A, fontsize = 16) 
        #y-axis lable
        plt.ylabel("Frequency of ", fontsize = 16)
        #Legend of graph
        plt.legend(loc = 'upper left')
        #Title of graph
        plt.title("Histogram of " + self.A + " with unique combinations of " + self.D + " and " + self.C, loc = 'center')
        plt.show()
        return
    

#Overlapping Histogram Function 
    def overlap_histogram(self):
        #Import libraries
        import numpy as np
        from matplotlib import pyplot as plt
        
        #Create variable that we call the function to calculate the bin width
        bin = bin_width(self.A)
        
        #Start at value = bin[0], Stop at value = bin[1], Increment by value of bin[2]
        bins = np.array(np.arange(start = bin[0], stop = bin[1], step = bin[2]))
        #Create histogram
        plt.hist(data[self.A], bins, alpha = 0.5, label = self.A, color = "red")
        plt.hist(data[self.B], bins, alpha = 0.5, label = self.B, color = "blue")
        #x-axis label
        plt.xlabel("Variables", fontsize = 16)  
        #y-axis lable
        plt.ylabel("Frequency", fontsize = 16)
        #Legend of graph
        plt.legend(loc = 'upper left')
        #Title of graph
        plt.title("Overlapping Histogram of Variables " + self.A + " and " + self.B, loc = 'center')
        plt.show()

#Create an object from class Graphs that will have one parameter
histo = Graphs('YRONJOB', None, None, None)
#Call histogram() function to apply to object
histo.histogram()