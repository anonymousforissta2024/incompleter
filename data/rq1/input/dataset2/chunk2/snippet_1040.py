#Source: https://stackoverflow.com/questions/50157962/python3-typeerror-list-indices-must-be-integers-or-slices-not-str
for item in server_list:
  for element in item :
    if element == selected_env :
       host_list=item[selected_env]  