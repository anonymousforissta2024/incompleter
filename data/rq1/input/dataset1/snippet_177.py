# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import json
    _l_(1539769)

except ImportError:
    pass

_c_(1539775, _a_(1539771, _n_(1539770, "json", lambda: json), "dumps"), _n_(1539772, "your_object", lambda: your_object), default=lambda __o: _a_(1539774, _n_(1539773, "__o", lambda: __o), "__dict__"))
_l_(1539776)
try:
    import json
    _l_(1539778)

except ImportError:
    pass
try:
    from dataclasses import dataclass
    _l_(1539780)

except ImportError:
    pass


@_n_(1539781, "dataclass", lambda: dataclass)
class Company:
    _l_(1539786)

    id: _n_(1539782, "int", lambda: int)
    _l_(1539783)
    name: _n_(1539784, "str", lambda: str)
    _l_(1539785)

@_n_(1539787, "dataclass", lambda: dataclass)
class User:
    _l_(1539796)

    id: _n_(1539788, "int", lambda: int)
    _l_(1539789)
    name: _n_(1539790, "str", lambda: str)
    _l_(1539791)
    email: _n_(1539792, "str", lambda: str)
    _l_(1539793)
    company: _n_(1539794, "Company", lambda: Company)
    _l_(1539795)


company = _c_(1539798, _n_(1539797, "Company", lambda: Company), id=1, name="Example Ltd")
_l_(1539799)
user = _c_(1539802, _n_(1539800, "User", lambda: User), id=1, name="John Doe", email="john@doe.net", company=_n_(1539801, "company", lambda: company))
_l_(1539803)


_c_(1539809, _a_(1539805, _n_(1539804, "json", lambda: json), "dumps"), _n_(1539806, "user", lambda: user), default=lambda __o: _a_(1539808, _n_(1539807, "__o", lambda: __o), "__dict__"))
_l_(1539810)

{
  "id": 1, 
  "name": "John Doe", 
  "email": "john@doe.net", 
  "company": {
    "id": 1, 
    "name": "Example Ltd"
  }
}
_l_(1539811)

