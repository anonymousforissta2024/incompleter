#Source: https://stackoverflow.com/questions/43747198/typeerror-cant-convert-int-object-to-str-implicitly-sorting-array-issue
def main ():
    rainfall = rainInput ()
    totalRain = totalRainfall (rainfall)
    average_Rainfall = averageRainfall (totalRain)
    highestMonth, highestMonthly = highestMonthNumber (rainfall)
    lowestMonth, lowestMonthly = lowestMonthNumber (rainfall)
    print #this is for spacing output
    print ('The total rainfall for the year was: ' +str(totalRain) + ' inche(s)')
    print #this is for spacing output
    print ('The average rainfall for the year was: ' +str(average_Rainfall) +\
          ' inche(s)') 
    print #this is for spacing in output
    print ('The highest amount of rain was', highestMonthly, 'in' , highestMonth)
    print #this is for spacing in output
    print ('The lowest amount of rain was', lowestMonthly, 'in' , lowestMonth)

def rainInput ():
    rainfall = ['January','Febuary','March','April','May','June','July','August'\
    ,'September','October','November','December']
    month = 0
    while month < len(rainfall):
        rainfall[month] = input ('Please enter the amount for month ' + str\
        (month + 1) + ': ')
        month += 1

    return rainfall

def totalRainfall (rainfall):
    totalRain = 0
    month = 0
    while month < len(rainfall):
        totalRain = rainfall[month] + totalRain
        month += 1

    return totalRain

def averageRainfall (totalRain):
    average_Rainfall = totalRain / 12

    return average_Rainfall

def highestMonthNumber (rainfall):
    month = ['January','Febuary','March','April','May','June','July','August'\
                ,'September','October','November','December']
    highestMonthly = 0
    for m, n in enumerate(rainfall):
        if n > highestMonthly:
            highestMonthly = n
            highestMonth = m

    return month[highestMonth], highestMonthly

def lowestMonthNumber (rainfall):
    month = ['January','Febuary','March','April','May','June','July','August'\
                ,'September','October','November','December']
    lowestMonthly = 0
    for m, n in enumerate(rainfall):
        if n < lowestMonthly:
            lowestMonthly = n
            lowestMonth = m

    return month[lowestMonth], lowestMonthly

main()