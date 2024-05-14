#Source: https://stackoverflow.com/questions/71921746/typeerror-list-indices-must-be-integers-or-slices-not-str-python-zabbixapi
for i in range(len(geteventlist)):
    i['host'] = i['hosts']['host']
    i['hostid'] = i['hosts']['hostid']
    i['location'] = i['hosts']['name']
    del i['hosts']