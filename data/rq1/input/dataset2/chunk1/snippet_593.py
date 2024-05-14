#Source: https://stackoverflow.com/questions/58418821/xml-parsing-error-attributeerror-nonetype-object-has-no-attribute-text
a = root3.xpath('//*[local-name()="claim-text"]/text()')
print(a, flush=True)