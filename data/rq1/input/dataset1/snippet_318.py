# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/1059559/split-strings-into-words-with-multiple-word-boundary-delimiters
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
join = lambda x: _c_(1538282, _n_(1538280, "sum", lambda: sum), _n_(1538281, "x", lambda: x),[])  # a.k.a. flatten1([[1],[2,3],[4]]) -> [1,2,3,4]
_l_(1538283)  # a.k.a. flatten1([[1],[2,3],[4]]) -> [1,2,3,4]
# ...alternatively...
join = lambda lists: [_n_(1538284, "x", lambda: x) for l in _n_(1538285, "lists", lambda: lists) for x in _n_(1538286, "l", lambda: l)]
_l_(1538287)

fragments = [_n_(1538288, "text", lambda: text)]
_l_(1538289)
for token in _n_(1538290, "tokens", lambda: tokens):
    _l_(1538299)

    fragments = _c_(1538297, _n_(1538291, "join", lambda: join), (_c_(1538295, _a_(1538293, _n_(1538292, "f", lambda: f), "split"), _n_(1538294, "token", lambda: token)) for f in _n_(1538296, "fragments", lambda: fragments)))
    _l_(1538298)

