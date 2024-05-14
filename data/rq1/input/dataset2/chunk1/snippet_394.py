#Source: https://stackoverflow.com/questions/58418821/xml-parsing-error-attributeerror-nonetype-object-has-no-attribute-text
import xml.etree.ElementTree as ET

root = ET.fromstring(my_xml_file)

u = root.find(".//name").text.rstrip()
print("Name: %s\n" % u)