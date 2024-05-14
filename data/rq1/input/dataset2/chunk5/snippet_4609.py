#Source: https://stackoverflow.com/questions/54547986/why-am-i-getting-nameerror-when-accessing-a-function
class ArmstrongNumber:

    def cubesum(num):
        return sum([int(i)**3 for i in list(str(num))])

    def PrintArmstrong(num):
        if cubesum(num) == num:
            return "Armstrong Number"
        return "Not an Armstrong Number"

    def Armstrong(num):
        if cubesum(num) == num:
            return True
        return False

[i for i in range(1000) if ArmstrongNumber.Armstrong(i)] # this return NameError