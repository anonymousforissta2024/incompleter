#Source: https://stackoverflow.com/questions/69930885/typeerror-module-object-is-not-callable-py-3
import flask
import _thread

app = flask.Flask('Keep Alive')

@app.route('/')
def home():
    return "I'm alive"

def run():
  app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = _thread(target=run)
    t.start()