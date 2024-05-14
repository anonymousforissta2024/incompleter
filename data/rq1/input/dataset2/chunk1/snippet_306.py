#Source: https://stackoverflow.com/questions/45860455/bottlepy-throws-typeerror-after-changing-server-to-cheroot
from bottle import Bottle, run
app = Bottle()

options = {
'certfile':'cacert.pem',
'keyfile':'privkey.pem',
}

run(app, host='localhost', port=8080, debug=True, server='cheroot', options=options)