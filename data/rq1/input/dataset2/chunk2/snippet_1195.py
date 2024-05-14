#Source: https://stackoverflow.com/questions/31912643/typeerror-cant-convert-bytes-object-to-str-implicitly-in-python
tree = ET.ElementTree(element_table)
xml = ET.tostring(element_table)
xml = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?><?xml-  stylesheet type=\"text/xsl\" href=\".\/xsl\/brsdk.xsl\"?>" + xml
obis_file = open( "OBIS_Support_Chart_" + sdk_version.replace( ".","_" ) +   ".xml", "w" )
obis_file.write( xml.decode('utf8') )