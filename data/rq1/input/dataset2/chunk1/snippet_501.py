#Source: https://stackoverflow.com/questions/5512811/builtins-typeerror-must-be-str-not-bytes
# -*- coding: utf-8 -*-
import time
from datetime import date
from lxml import etree
from collections import OrderedDict

# Create the root element
page = etree.Element('results')

# Make a new document tree
doc = etree.ElementTree(page)

# Add the subelements
pageElement = etree.SubElement(page, 'Country',Tim = 'Now', 
                                      name='Germany', AnotherParameter = 'Bye',
                                      Code='DE',
                                      Storage='Basic')
pageElement = etree.SubElement(page, 'City', 
                                      name='Germany',
                                      Code='PZ',
                                      Storage='Basic',AnotherParameter = 'Hello')
# For multiple multiple attributes, use as shown above

# Save to XML file
outFile = open('output.xml', 'w')
doc.write(outFile) 