#Source: https://stackoverflow.com/questions/75353814/python-google-or-tools-surgical-booking-attributeerror-dataframe
from __future__ import print_function
from ortools.sat.python import cp_model
import pandas as pd
import sys
import math



#

# Parameters
targetOvertimeFrequency = 0.2
targetUndertimeFrequency = 0
undertimeCostWeight = 1
overtimeCostWeight = 1

arguments = sys.argv
excelInputFile = 'input.xlsx'
excelOutputFile = 'output.xlsx'

overtimeBlockLength = 15 # length of overtime blocks in minutes
noOfNursesPerBlock = 2.5 # number of nurses per overtime block
overtimeSalary = 75 # pay by block for overtime nurses

# Optional: get excel filenames from command line argument
if (len(arguments) > 1):
    excelInputFile = str(arguments[1])
    excelOutputFile = str(arguments[2])


# Read data from an excel file
data = pd.read_excel(r'' + excelInputFile, header=4)
#
# Input data from excel sheet columns

dfP = pd.DataFrame(data, columns=["Procedure"])
dfP = dfP.iloc[:, :].values.tolist()
dfP = [x for y in dfP for x in y]

dfD = pd.DataFrame(data, columns=["Date"])
dfD = dfD.get_values()
dfD = [x for y in dfD for x in y]

dfE = pd.DataFrame(data, columns=["Book Dur"])
dfE = dfE.iloc[:, :].values.tolist()
dfE = [x for y in dfE for x in y]

dfA = pd.DataFrame(data, columns=["Actual Dur"])
dfA = dfA.iloc[:, :].values.tolist()
dfA =  [x for y in dfA for x in y]

rawProcedures = [] # a list of each procedure performed
procedureTypes = [] # a list of all theprocedure codes
rawDays = [] # a list of dates for each procedure performed
days = [] # a list of the dates in the data
rawExpectedTimes = [] # a list of scheduled times for each procedure performed
rawActualTimes = [] # a list of actual times for each procedure performed

# Input data into arrays
for i in range(len(dfE)):
    if str(dfE[i]) != 'nan':
        if dfD[i] not in days:
            days.append(dfD[i])
        rawExpectedTimes.append(dfE[i])
        rawDays.append(dfD[i])
        rawActualTimes.append(dfA[i])
        rawProcedures.append(dfP[i])
        if dfP[i] not in procedureTypes:
            procedureTypes.append(dfP[i])

procedureTypes.sort() # sort procedure types alphabetically

proceduresPerDay = {w: [] for w in days} # a map from a day to a list of procedures performed on that day
for i in range(len(rawDays)):
    proceduresPerDay[rawDays[i]].append(rawProcedures[i])


expectedTimes = {w: [] for w in days} # a map from a day to a list of booking times for that day
for i in range(len(rawDays)):
    expectedTimes[rawDays[i]].append(rawExpectedTimes[i])

actualTimes = {w: [] for w in days} # a map from a day to a list of actual procedure times for that day
for i in range(len(rawDays)):
    actualTimes[rawDays[i]].append(rawActualTimes[i])

#    ­
# Pre-processing

originalBookTimes = {p: 0 for p in procedureTypes} # a map with average booking times for each procedue
for p in procedureTypes:
    counter = 0
    for i in range(len(rawDays)):
        if p == rawProcedures[i]:
            counter +=  1
            originalBookTimes[p] += rawExpectedTimes[i]
    originalBookTimes[p] = int(originalBookTimes[p]/counter)

expectedTotalTime = {} # a map from a day to the sum of booking times for that day
for day in days:
    expectedTotalTime[day] = 0
    for time in expectedTimes[day]:
        expectedTotalTime[day] += time

actualTotalTime = {} # a map from a day to the sum of actual procedure times for that day
for day in days:
    actualTotalTime[day] = 0
    for time in actualTimes[day]:
        actualTotalTime[day] += time

currentOvertimeCount = 0 # counts how many days the room went overtime
currentUndertimeCount = 0 # counts how many days the room went undertime
for day in days:
    if expectedTotalTime[day] + 0 < actualTotalTime[day]: currentOvertimeCount += 1
    elif actualTotalTime[day] + 15 < expectedTotalTime[day]: currentUndertimeCount +=  1

minProcedureTime = {p: 1440 for p in procedureTypes} # a map from a procedure to its minimum case time
maxProcedureTime = {p: 0 for p in procedureTypes} # a map from a procedure to its maximum case time

for i in range(len(rawDays)):
    if rawActualTimes[i] < minProcedureTime[rawProcedures[i]]: minProcedureTime[rawProcedures[i]] = rawActualTimes[i]
    if rawActualTimes[i] > maxProcedureTime[rawProcedures[i]]:
        maxProcedureTime[rawProcedures[i]] = rawActualTimes[i]
        
count = len(days) # number of days
 
#

# Model
print("Starting model optimisation", file=sys.stderr)

# Decision variables
model = cp_model.CpModel() # Create the model

procedureSchedulingTimes = {} # Create a decision variable for the scheduling time of each procedure type
for p in procedureTypes:
    procedureSchedulingTimes[p] = model.NewIntVar(int(minProcedureTime[p]),
     int(maxProcedureTime[p]),
                                "procedureSchedulingTime" + str(p))

totalScheduledTime = {} # The total time scheduled for each day
overtimeTriggers={} # Set to 1 if overtime for each day
undertimeTriggers = {} # Set to 1 if undertime for each day
for day in days:
    totalScheduledTime[day] = model.NewIntVar(0, 1000, "day"+ str(day))
    overtimeTriggers[day] = model.NewIntVar(0, 1, "overtimeTrigger" + str(day))
    undertimeTriggers[day] = model.NewIntVar(0, 1, "undertimeTrigger" + str(day))

overtimeCount = model.NewIntVar(0, 1000, "overtimeCount") # Number of days that went overtime
undertimeCount = model.NewIntVar(0, 1000, "undertimeCount") # Number of days that went undertime
overtimeCost = model.NewIntVar(-1000, 1000, "overtimeCost") # Overtime cost
undertimeCost = model.NewIntVar(-1000, 1000, "undertimeCost") # Undertime cost
absOvertimeCost = model.NewIntVar(0, 100, "absOvertimeCost") # !overtime costl
absUndertimeCost = model.NewIntVar(0, 100, "absUndertimeCost") # lundertime costl
finalCost = model.NewIntVar(0, 100, "finalCost") # final cost is sum of overtime and undertime costs

#-------------------
# Constraints
for day in days:
    # set totalScheduledTime to the sum of scheduled time in a day
    model.Add(totalScheduledTime[day] == (sum(procedureSchedulingTimes[i] for i in proceduresPerDay[day])))

    # set overtime trigger to 1 if overtime
    model.Add(1000 * overtimeTriggers[day] >= int(actualTotalTime[day]) - totalScheduledTime[day] - 0 - 1)
 
    # set overime trigger to O if not overtime
    model.Add(1500 * (1 - overtimeTriggers[day]) >= totalScheduledTime[day] - int(actualTotalTime[day]) + 0)

    # set undertime trigger to 1 if undertime
    model.Add(1000 * undertimeTriggers[day] >= totalScheduledTime[day] - 15 - int(actualTotalTime[day]) - 1)
    # set undertime trigger to O if not undertime
    model.Add(1000 * (1 - undertimeTriggers[day]) >= int(actualTotalTime[day]) - totalScheduledTime[day] + 15)

model.Add(overtimeCount == (sum(overtimeTriggers[day] for day in days))) # count how many days went overtime
model.Add(undertimeCount == (sum(undertimeTriggers[day] for day in days))) # count how many days went undertime

model.Add((overtimeCost == overtimeCount - int(count * targetOvertimeFrequency))) #calculate overtime cost
model.Add((undertimeCost == undertimeCount - int(count * targetUndertimeFrequency))) #calculate undertime cost

# calculate absolute value of overtime cost
model.AddAbsEquality(absOvertimeCost, int(overtimeCostWeight) * overtimeCost)
# calculate absolute value of undertime cost
model.AddAbsEquality(absUndertimeCost, int(undertimeCostWeight) * undertimeCost)
model.Add((finalCost == overtimeCost + undertimeCost)) # calculate final cost

model.Minimize(finalCost) # Objective is to minimize final cost

solver= cp_model.CpSolver()
print("Starting to solve", file=sys.stderr)
status = solver.Solve(model)

#

# Print output to console and excel sheet
if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("Success!")
    rows= ["Number of days","Number of cases","Original overtime frequency","Original undertime frequency","Model overtime frequency",
            "Model undertime frequency","Model cases achieved", "Original Overtime Minutes Used","Model Overtime Minutes Used",
            "Original Overtime Cost","Model Overtime Cost", "Original OR minutes used", "Model OR minutes used", "","Procedure Type"] + procedureTypes

    dashboard= pd.DataFrame(index=rows,columns=["A", "B", "C",])

for r in rows:
    dashboard.at[r,"A"]= r

#-------------------
# Output basic stats
dashboard.at["", ""] = ""
dashboard.at["Number of days", "B"] = count
print("number of days: ", count)
dashboard.at["Number of cases", "B"] = len(rawExpectedTimes)

print("number of cases: ", len(rawExpectedTimes))
dashboard.at["Original overtime frequency", "B"] = round(currentOvertimeCount / count, 2)
print("current overtime frequency: %.Of%%" % (100 * currentOvertimeCount / count))
dashboard.at["Original undertime frequency", "B"] = round(currentUndertimeCount / count,2)
print("current undertime frequency: %.Of%%" % (100 * currentUndertimeCount/ count))
dashboard.at["Model overtime frequency", "B"] = round(solver.Value(overtimeCount) /count, 2)
print("model overtime frequency: %.Of%%" % (100 * solver.Value(overtimeCount) / count))
dashboard.at["Model undertime frequency", "B"] = round(solver.Value(undertimeCount) /count, 2)
print("model undertime frequency: %.Of%%" % (100 * solver.Value(undertimeCount) / count))

#-------------------
# Output overtime minutes and overtime cost
originalOverMinutes = 0
modelOverMinutes = 0

originalCost = 0
modelCost = 0

for day in days:
    if solver.Value(totalScheduledTime[day]) < actualTotalTime[day]:
        modelOverMinutes += actualTotalTime[day] - solver.Value(totalScheduledTime[day])
        modelCost += math.ceil((actualTotalTime[day] - solver.Value(totalScheduledTime[day])) / overtimeBlocklength) * noOfNursesPerBlock * overtimeSalary
    if expectedTotalTime[day] < actualTotalTime[day]:
        originalOverMinutes += actualTotalTime[day] - expectedTotalTime[day]
        originalCost += math.ceil((actualTotalTime[day] - expectedTotalTime[day]) / overtimeBlocklength) * noOfNursesPerBlock * overtimeSalary


print("Original overtime minutes used: ", originalOverMinutes)
dashboard.at["Original Overtime Minutes Used", "B"] = originalOverMinutes
print("Model overtime minutes used: ", modelOverMinutes)
dashboard.at["Model Overtime Minutes Used", "B"] = modelOverMinutes

print("Original Overtime cost: ", originalCost)
dashboard.at["Original Overtime Cost", "B"] = originalCost
print("Model overtime cost: ", modelCost)
dashboard.at["Model Overtime Cost", "B"] = modelCost

print("\n")

#-------------------
# Output original and machine learning scheduling times for each procedure
dashboard.at["Procedure Type", "B"] = "Original Time"
dashboard.at["Procedure Type", "C"] = "Machine Learning Time"
for p in procedureTypes:
    print(p + ": " + "%/d" % solver.Value(procedureSchedulingTimes[p]))
    dashboard.at[p, "B"] = originalBookTimes[p]
    dashboard.at[p, "C"] = solver.Value(procedureSchedulingTimes[p])

#-------------------
# Output cases completed with model and OR minutes used by original and machine learning methods
totalNoCases = 0
originalCases = 0
modelCases = 0
originalMinutes = 0
modelMinutes = 0
totalMinutes = 0

print("\n")
for day in days:
    noOfCases = len(actualTimes[day])
    totalNoCases += noOfCases

    originalMinutes += actualTotalTime[day]
    modelMinutes += solver.Value(totalScheduledTime[day])

    ORTime = 450 - (noOfCases - 1) * 15
    totalMinutes += ORTime

    originalTime = (ORTime - actualTotalTime[day])
    modelTime = (ORTime - solver.Value(totalScheduledTime[day]))
    originalCases += noOfCases
    if originalTime < 0:
        for i in reversed(range(len(actualTimes[day]))):
            originalTime += actualTimes[day][i]
            originalCases -= 1
            if originalTime > 0:
                break
        modelCases += noOfCases
        if modelTime < 0:
            for i in reversed(range(len(actualTimes[day]))):
                modelTime += actualTimes[day][i]
                modelCases -= 1
                if modelTime > 0:
                    break

    print("Cases achieved with machine learning model: %.Of%%" % (100 * modelCases/ totalNoCases))
    dashboard.at["Model cases achieved", "B"] = round(modelCases / totalNoCases, 2)
    print("OR minutes used with original model: %.Of%%" % (100 * originalMinutes/totalMinutes))
    dashboard.at["Original OR minutes used", "B"] = round(originalMinutes / totalMinutes, 2)
    print("OR minutes used with machine learning model: %.Of%%" % (100 * modelMinutes /
totalMinutes))
    dashboard.at["Model OR minutes used", "B"] = round(modelMinutes / totalMinutes, 2)

    dashboard.to_excel(r'' + excelOutputFile, index=False)

else:

    print("No feasible solution found.")
 
 