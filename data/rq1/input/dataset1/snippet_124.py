# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2835559/why-cant-python-parse-this-json-data
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
{
    "maps": [
        {
            "id": "blabla",
            "iscategorical": "0"
        },
        {
            "id": "blabla",
            "iscategorical": "0"
        }
    ],
    "masks": [{
        "id": "valore"
    }],
    "om_points": "value",
    "parameters": [{
        "id": "valore"
    }]
}
_l_(1548473)
try:
    import json
    _l_(1548475)

except ImportError:
    pass
try:
    from pprint import pprint
    _l_(1548477)

except ImportError:
    pass
with _c_(1548479, _n_(1548478, "open", lambda: open), 'data.json') as data_file:
    _l_(1548485)

    data_item = _c_(1548483, _a_(1548481, _n_(1548480, "json", lambda: json), "load"), _n_(1548482, "data_file", lambda: data_file))
    _l_(1548484)
_c_(1548488, _n_(1548486, "pprint", lambda: pprint), _n_(1548487, "data_item", lambda: data_item))
_l_(1548489)

{'maps': [{'id': 'blabla', 'iscategorical': '0'},
          {'id': 'blabla', 'iscategorical': '0'}],
 'masks': [{'id': 'valore'}],
 'om_points': 'value',
 'parameters': [{'id': 'valore'}]}
_l_(1548490)

_n_(1548491, "valore", lambda: valore)
_l_(1548492)

