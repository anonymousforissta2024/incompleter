# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/749796/pretty-printing-xml-in-python
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import xml.dom.minidom
    _l_(1539159)

except ImportError:
    pass

file = _c_(1539161, _n_(1539160, "open", lambda: open), "./content.xml", 'r')
_l_(1539162)
xml_string = _c_(1539165, _a_(1539164, _n_(1539163, "file", lambda: file), "read"))
_l_(1539166)
_c_(1539169, _a_(1539168, _n_(1539167, "file", lambda: file), "close"))
_l_(1539170)

parsed_xml = _c_(1539175, _a_(1539173, _a_(1539172, _a_(1539171, xml, "dom"), "minidom"), "parseString"), _n_(1539174, "xml_string", lambda: xml_string))
_l_(1539176)
pretty_xml_as_string = _c_(1539179, _a_(1539178, _n_(1539177, "parsed_xml", lambda: parsed_xml), "toprettyxml"))
_l_(1539180)

file = _c_(1539182, _n_(1539181, "open", lambda: open), "./content_new.xml", 'w')
_l_(1539183)
_c_(1539187, _a_(1539185, _n_(1539184, "file", lambda: file), "write"), _n_(1539186, "pretty_xml_as_string", lambda: pretty_xml_as_string))
_l_(1539188)
_c_(1539191, _a_(1539190, _n_(1539189, "file", lambda: file), "close"))
_l_(1539192)

