#Source: https://stackoverflow.com/questions/35026280/curangle-throwing-this-error-typeerror-float-argument-must-be-a-string-or
    #Update the solar file for reporting
logsolar = open('/tools/inputs/solarvalues.txt','w')
writeline=("[myvars]\n")
logsolar.write(writeline)
writeline=("solar_heading: " + str(round((float(getsolarheading())),1)) + "\n")
logsolar.write(writeline)
writeline=("solar_elevation: " + str(round((float(getsolarangle())),1))+ "\n")
logsolar.write(writeline)
writeline=("actual_elevation: " + str(round((float(getcurangle())),1))+ "\n")
logsolar.write(writeline)
writeline=("actual_heading: " + str(round((float(getcurheading())),1))+ "\n")
logsolar.write(writeline)
logsolar.close()