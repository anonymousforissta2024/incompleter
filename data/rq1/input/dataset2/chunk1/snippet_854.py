#Source: https://stackoverflow.com/questions/44723602/attributeerror-str-object-has-no-attribute-seek-using-textfsm-module-regex
from netmiko import ConnectHandler      
from textfsm import *  

cisco_device = { 'device_type' : 'cisco_ios', 'ip' : 'x.x.x.x', 'username':'****0', 'password':'***9'}
net_connect = ConnectHandler(**cisco_device)

fo=("test.txt" , 'w')

output = net_connect.send_command("show ip int brief")

re_table = TextFSM('xr_show_int_br','r')     

data = re_table.ParseText(output)

print (output)
print(re_table.header)

for test in (re_table.header):
          fo.write(test)

fo.write("\n")

for row in data:
          for temp_row in data:
              fo.write(temp_row)
          fo.write("\n")


fo.close