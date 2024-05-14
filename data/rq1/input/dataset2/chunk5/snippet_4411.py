#Source: https://stackoverflow.com/questions/57987388/typeerror-unsupported-operand-types-for-str-and-str-how-to-solve-it
import wmi
c = wmi.WMI ()

for process in c.Win32_Process ():
    #print (process.Name)
    if process.Name == "chrome.exe" & process.Name > 1:
        print (process.Name)