#Source: https://stackoverflow.com/questions/56708529/typeerror-when-assigning-node-attributes-in-networkx
for e in emplyoees:
    nx.set_node_attributes(B, name='type', values='employee')

for m in movies:
    nx.set_node_attributes(B, name='type', values='movie')