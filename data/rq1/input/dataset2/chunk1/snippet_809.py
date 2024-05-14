#Source: https://stackoverflow.com/questions/55695479/why-cant-i-sort-a-list-of-dicts-in-3-x-why-do-i-get-typeerror-not-suppor
server_list = []

for server in res["aggregations"]["hostname"]["buckets"]:
    temp_obj = []
    temp_obj.append({"name":server.key})        
    temp_obj.append({"stat": server["last_log"]["hits"]["hits"][0]["_source"][system].stat})
    server_list.append(temp_obj)
    server_list.sort(key=lambda x: x[0], reverse=False)