#Source: https://stackoverflow.com/questions/64511584/parsing-xml-in-python-typeerror-str-object-is-not-callable
import xml.etree.ElementTree as ET

data = '''<person>
<date>Wednesday, Oct 14 2020 1:03AM</date>
<email hide="yes" />
<username>John Doe</username>
</person>'''


tree = ET.fromstring(data)
print("Date:", tree.find('date').text())
print("Email attr:", tree.find('email').get('hide'))