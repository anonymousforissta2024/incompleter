#Source: https://stackoverflow.com/questions/58418821/xml-parsing-error-attributeerror-nonetype-object-has-no-attribute-text
root = ET.fromstring(usr_str)

u = root.find(".//claim-text").text.rstrip()
print("Abstract: %s\n" % u)