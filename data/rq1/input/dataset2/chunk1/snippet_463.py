#Source: https://stackoverflow.com/questions/69390842/parsing-namespace-xml-generates-attributeerror-str-object-has-no-attribute-t
for ecu_container in root.findall('.//{http://autosar.org/schema/r4.0}ECUC-CONTAINER-VALUE'):
    short_name = ecu_container.find('.//{http://autosar.org/schema/r4.0}SHORT-NAME').text
    if(short_name == component):
        value = ecu_container.find('.//{http://autosar.org/schema/r4.0}VALUE').text
        value.text = str(imageState)