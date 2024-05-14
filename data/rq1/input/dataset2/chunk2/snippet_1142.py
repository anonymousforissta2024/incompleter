#Source: https://stackoverflow.com/questions/52045772/typeerror-endturn-missing-1-required-positional-argument-self
class turns():

    def endturn(self):
        global movePoints
        print("Turn Ended: \nRecruitment Report: {}".format(Recruited))
        movePoints = 20

x = 50
y = 50
speed = 10
movePoints = 20
movePointLost = 1
Recruited = 0

turns.endturn()