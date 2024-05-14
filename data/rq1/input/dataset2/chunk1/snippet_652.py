#Source: https://stackoverflow.com/questions/58829152/docker-nameerror-name-app-is-not-defined
#importing dependencies
from flask import Flask

#initializing the name of the application
app = Flask(__name__)

@app.route('/')

def hello(parameter_list):
    return 'Hello, this is my first try on Docker'

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug= True)