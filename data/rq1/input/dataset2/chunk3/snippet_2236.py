#Source: https://stackoverflow.com/questions/67638541/f5-tlm-typeerror-object-of-type-nodes-is-not-json-serializable
from f5.bigip import ManagementRoot
import json 

user = 'admin'
password = 'secret'
f5_ip = '10.0.0.10'
partition = 'PART1'


mgmt = ManagementRoot(f5_ip, user, password)
ltm = mgmt.tm.ltm

nodes = ltm.nodes.get_collection()

for node in nodes:
    node_dict = node.raw
    node_json = json.dumps(node_dict, indent=4)
    print(node_json)
    