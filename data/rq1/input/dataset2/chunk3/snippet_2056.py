#Source: https://stackoverflow.com/questions/44726772/attributeerror-tuple-object-has-no-attribute-write-error-while-writing-into
from netmiko import ConnectHandler      
from textfsm import * 

cisco_device = { 'device_type' : 'cisco_ios', 'ip' : 'x.x.x.x', 'username':'gtomy200', 'password':'xxxxx'}
net_connect = ConnectHandler(**cisco_device)

fo=("testme.txt" , 'w')

output = net_connect.send_command("show int brief")

re_table = TextFSM(open('xr_show_int_br','r'))    

data = re_table.ParseText(output)

print (output)

for s in re_table.header:

          fo.write("%s;" %s)

fo.write("\n")

for row in data:
        print (row)
        for s in row:

                fo.write("%s" %s)
                fo.write("\n")

fo.close()