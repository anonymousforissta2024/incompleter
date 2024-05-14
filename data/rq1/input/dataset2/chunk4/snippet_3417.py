#Source: https://stackoverflow.com/questions/51370082/nameerror-name-is-not-defined-passing-function-return-as-input-to-another
import csv
def CreateDict(filename):
    UsrDict = {}
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=':')
        for row in readCSV:
            UsrDict[row[0]]=row[1]
        return UsrDict


def CreateHumanUsrNameDict(UsrDict):
    HumanUsrDict={}
    for k, v in HumanUsrDict.items():
        if v == len(4):
            HumanUsrDict[k:v]
        print(HumanUsrDict)

if __name__=='__main__':
    CreateDict('Book1.csv')
    CreateHumanUsrNameDict(UsrDict)