# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4406501/change-the-name-of-a-key-in-dictionary
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
def lowercase_keys(obj):
  _l_(1544621)

  if _c_(1544584, _n_(1544581, "isinstance", lambda: isinstance), _n_(1544582, "obj", lambda: obj), _n_(1544583, "dict", lambda: dict)):
    _l_(1544618)

    obj = {_c_(1544587, _a_(1544586, _n_(1544585, "key", lambda: key), "lower")): _n_(1544588, "value", lambda: value) for key, value in _c_(1544591, _a_(1544590, _n_(1544589, "obj", lambda: obj), "items"))}
    _l_(1544592)
    for key, value in _c_(1544595, _a_(1544594, _n_(1544593, "obj", lambda: obj), "items")):
      _l_(1544617)

      if _c_(1544599, _n_(1544596, "isinstance", lambda: isinstance), _n_(1544597, "value", lambda: value), _n_(1544598, "list", lambda: list)):
        _l_(1544610)

        for idx, item in _c_(1544602, _n_(1544600, "enumerate", lambda: enumerate), _n_(1544601, "value", lambda: value)):
          _l_(1544609)

          _n_(1544603, "value", lambda: value)[_n_(1544604, "idx", lambda: idx)] = _c_(1544607, _n_(1544605, "lowercase_keys", lambda: lowercase_keys), _n_(1544606, "item", lambda: item))
          _l_(1544608)
      _n_(1544611, "obj", lambda: obj)[_n_(1544612, "key", lambda: key)] = _c_(1544615, _n_(1544613, "lowercase_keys", lambda: lowercase_keys), _n_(1544614, "value", lambda: value))
      _l_(1544616)
  aux = _n_(1544619, "obj", lambda: obj) 
  _l_(1544620) 
  return aux 

json_str = {"FOO": "BAR", "BAR": 123, "EMB_LIST": [{"FOO": "bar", "Bar": 123}, {"FOO": "bar", "Bar": 123}], "EMB_DICT": {"FOO": "BAR", "BAR": 123, "EMB_LIST": [{"FOO": "bar", "Bar": 123}, {"FOO": "bar", "Bar": 123}]}}
_l_(1544622)

_c_(1544625, _n_(1544623, "lowercase_keys", lambda: lowercase_keys), _n_(1544624, "json_str", lambda: json_str))
_l_(1544626)


_n_(1544627, "Out", lambda: Out)[0]: {'foo': 'BAR',
 'bar': 123,
 'emb_list': [{'foo': 'bar', 'bar': 123}, {'foo': 'bar', 'bar': 123}],
 'emb_dict': {'foo': 'BAR',
  'bar': 123,
  'emb_list': [{'foo': 'bar', 'bar': 123}, {'foo': 'bar', 'bar': 123}]}}
_l_(1544628)

