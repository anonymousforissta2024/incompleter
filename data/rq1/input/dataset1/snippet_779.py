# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/4789837/how-to-terminate-a-python-subprocess-launched-with-shell-true
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
if _c_(1542730, _n_(1542727, "isinstance", lambda: isinstance), _n_(1542728, "command", lambda: command), _n_(1542729, "unicode", lambda: unicode)):
    _l_(1542735)

    cmd = _c_(1542733, _a_(1542732, _n_(1542731, "command", lambda: command), "encode"), 'utf8')
    _l_(1542734)
args = _c_(1542739, _a_(1542737, _n_(1542736, "shlex", lambda: shlex), "split"), _n_(1542738, "cmd", lambda: cmd))
_l_(1542740)

p = _c_(1542748, _a_(1542742, _n_(1542741, "subprocess", lambda: subprocess), "Popen"), _n_(1542743, "args", lambda: args), stdout=_a_(1542745, _n_(1542744, "subprocess", lambda: subprocess), "PIPE"), stderr=_a_(1542747, _n_(1542746, "subprocess", lambda: subprocess), "STDOUT"))
_l_(1542749)

