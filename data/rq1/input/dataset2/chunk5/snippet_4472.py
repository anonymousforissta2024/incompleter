#Source: https://stackoverflow.com/questions/49844007/nameerror-name-temp-output-is-not-defined
def Read_Temp():
        lines = Temp_Raw()
        while lines[0].strip()[-3:] != 'YES':
             time.sleep(0.2)
             lines = Temp_Raw()
        temp_output = lines[1].find('t=')
        if temp_output != -1:
            temp_sting = lines[1].strip()[temp_output+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_c, temp_f
while True:
     print(Read_Temp())
     time.sleep(1)