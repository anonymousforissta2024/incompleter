#Source: https://stackoverflow.com/questions/48802655/xml-etree-elementtree-parse-attributeerror-list-object-has-no-attribute-ge
import xml.etree.ElementTree as ET

tree = ET.parse('sample.xml')   
root = tree.getroot()

for elem in root:

    print(elem.findall('alarmTime').get('id'))