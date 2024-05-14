#Source: https://stackoverflow.com/questions/50157962/python3-typeerror-list-indices-must-be-integers-or-slices-not-str
selected_env='mydev2'
server_list=[{'mydev': ['192.168.56.102', '192.168.56.102', '192.168.56.102']}, {'mydev2': ['192.168.56.102', '192.168.56.102', '192.168.56.102']}]         
for item in server_list :
    host_list=[item for item in server_list[selected_env] if selected_env in server_list]

print(host_list)