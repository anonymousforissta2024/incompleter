#Source: https://stackoverflow.com/questions/63092814/typeerror-not-supported-between-instances-of-int-and-tuple-python-pand
def int_checker_projects(columnName):
    intArray = []
    for value in projectsFileData[columnName]:
        try:
            intArray.append(int(value))
        except ValueError:
            sys.exit("ERROR: {0} in the {1} column is not an integer. Terminating Program.".format(value, columnName))
    return intArray

projectIDs = int_checker_projects('projectID')

for pid in zip(projectIDs):
    if pow(2, 64) < pid < 0:
        sys.exit("ERROR: projectID {0} must be an integer greater than zero and less than 2^64.".format(pid))