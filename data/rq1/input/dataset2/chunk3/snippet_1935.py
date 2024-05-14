#Source: https://stackoverflow.com/questions/67100743/dbus-error-unable-to-append-with-type-error-saying-list-indices-must-be-integer
@dbus.service.method("com.fsevenm.castboard.KaroWidget", in_signature='', out_signature="a{si}")
def get_screens(self):
    return [
        {
            "id": 1
        }
    ]