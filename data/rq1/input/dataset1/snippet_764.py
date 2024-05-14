# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/6567831/how-to-perform-or-condition-in-django-queryset
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    from django.db.models import Q
    _l_(1542306)

except ImportError:
    pass
_c_(1542314, _a_(1542309, _a_(1542308, _n_(1542307, "User", lambda: User), "objects"), "filter"), _c_(1542311, _n_(1542310, "Q", lambda: Q), income__gte=5000) | _c_(1542313, _n_(1542312, "Q", lambda: Q), income__isnull=True),category='income')
_l_(1542315)

