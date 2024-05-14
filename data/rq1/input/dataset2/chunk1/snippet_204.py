#Source: https://stackoverflow.com/questions/58418821/xml-parsing-error-attributeerror-nonetype-object-has-no-attribute-text
from lxml import etree
root = etree.XML(my_xml.encode('ascii'))
root2 = etree.XML(my_xml2.encode('ascii'))

root.xpath('//*[local-name()="name"]/text()')
root2.xpath('//*[local-name()="claim-text"]/text()')