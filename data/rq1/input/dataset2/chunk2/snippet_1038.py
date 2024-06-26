#Source: https://stackoverflow.com/questions/58086286/i-am-getting-attributeerror-type-object-observable-has-no-attribute-from
import sys
from rx import Observable

argv = Observable.from_(sys.argv[1:])
argv.subscribe(
    on_next=lambda i: print("on_next: {}".format(i)),
    on_error=lambda e: print("on_error: {}".format(e)),
    on_completed=lambda: print("on_completed")
)