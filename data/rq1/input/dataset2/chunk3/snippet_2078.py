#Source: https://stackoverflow.com/questions/63009363/name-error-data-is-not-defined-when-sending-post-request-values-from-react-to-fl
from flask import Flask, request, json


app = Flask(__name__)

@app.route('/api', methods=['GET','POST'])
def api():
        data = request.form['username']
print (data)