#Source: https://stackoverflow.com/questions/58783972/typeerror-error-while-checking-if-the-values-in-a-list-existed-in-a-dict
class SifFile():
    setting = {}
    interesting_param = ['Temp', 'Pressure']

    def __init__(self, get_param):
        self.File_Type = "Andor Technology Multi-Channel File"
        for k, v in get_param.items():            
            if SifFile.interesting_param in k:
                SifFile.setting[k] = v
                return SifFile.setting

get_parameter = {'Temp':75, 'Pressure':50, 'Helium':90, 'Exp':96}

sif = SifFile(get_parameter)