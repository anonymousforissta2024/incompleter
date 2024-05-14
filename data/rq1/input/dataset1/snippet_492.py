# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/12578908/separation-of-business-logic-and-data-access-in-django
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
class Book:
   _l_(1544958)

   author = _c_(1544951, _a_(1544950, models, "ForeignKey"), User)
   _l_(1544952)
   title = _c_(1544954, _a_(1544953, models, "CharField"), max_length=125)
   _l_(1544955)

   class Meta:
      _l_(1544957)

      app_label = "library"
      _l_(1544956)
try:
   from library.models import Book
   _l_(1544960)

except ImportError:
   pass

def get_books(limit=None, **filters):
   _l_(1544968)

   """ simple service function for retrieving books can be widely extended """
   aux = _c_(1544965, _a_(1544963, _a_(1544962, _n_(1544961, "Book", lambda: Book), "objects"), "filter"), **_n_(1544964, "filters", lambda: filters))[:_n_(1544966, "limit", lambda: limit)]  # list[:None] will return the entire list
   _l_(1544967)  # list[:None] will return the entire list
   return aux  # list[:None] will return the entire list
try:
   from library.services import get_books
   _l_(1544970)

except ImportError:
   pass

class BookListView(_n_(1544971, "ListView", lambda: ListView)):
   _l_(1544975)

   """ simple view, e.g. implement a _build and _apply filters function """
   queryset = _c_(1544973, _n_(1544972, "get_books", lambda: get_books))
   _l_(1544974)

