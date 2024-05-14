#Source: https://stackoverflow.com/questions/58260024/attributeerror-str-object-has-no-attribute-firstchild
import os
from xml.dom.minidom import parse

j=0
path = "C:/Users/User/Downloads"
quantity = []
# for every file in directory (path above)
for filename in os.listdir(path):
    if not filename.endswith('.xml'): continue
    fullname = os.path.join(path, filename) # add path and file together
    data = parse(fullname) # parses XML
    ordernum = data.getElementsByTagName('OrderNumber') # gets OrderNumber from XML
    print(ordernum[0].firstChild.nodeValue) # prints OrderNumber from XML
    quan = data.getElementsByTagName('OrderedQuantity') # same as above with OrderedQuantity
    k=0
    l=0
    for k, q in enumerate(quan):
        if q.firstChild.nodeValue != None:
            quantity.append(quan[k].firstChild.nodeValue)
    quantity.append("||separator||")
    for l, p in enumerate(ordernum):
        if p.firstChild.nodeValue != None:
            ordernum.append(ordernum[l].firstChild.nodeValue)
    ordernum.append("||separator||")