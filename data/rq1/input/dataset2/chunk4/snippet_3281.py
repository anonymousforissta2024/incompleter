#Source: https://stackoverflow.com/questions/72426111/python3-error-typeerror-not-supported-between-instances-of-str-and-int
config.plugins.Times.Updattime = ConfigIP(default=[0, 0], auto_jump=False)
config.plugins.Times.Updattime.value = self.Verif(config.plugins.Times.Updattime.value)

def Verif(self, Valist):
        if int(Valist[0]) < 10:
            if int(Valist[1]) < 10:
                Valist = ['0' + str(Valist[0]), '0' + str(Valist[1])]
            else:
                Valist = ['0' + str(Valist[0]), Valist[1]]
        elif int(Valist[1]) < 10:
            Valist = [Valist[0], '0' + str(Valist[1])]
        else:
            Valist = [Valist[0], Valist[1]]
        return Valist