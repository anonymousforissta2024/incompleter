# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/22676/how-to-download-a-file-over-http
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from parallel_sync import wget
    _l_(1543511)

except ImportError:
    pass
urls = ['http://something.png', 'http://somthing.tar.gz', 'http://somthing.zip']
_l_(1543512)
_c_(1543516, _a_(1543514, _n_(1543513, "wget", lambda: wget), "download"), '/tmp', _n_(1543515, "urls", lambda: urls))
_l_(1543517)
# or a single file:
_c_(1543521, _a_(1543519, _n_(1543518, "wget", lambda: wget), "download"), '/tmp', _n_(1543520, "urls", lambda: urls)[0], filenames='x.zip', extract=True)
_l_(1543522)

