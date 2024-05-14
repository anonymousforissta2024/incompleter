#Source: https://stackoverflow.com/questions/53784399/nameerror-name-key-is-not-definedunable-to-display-error-using-bottle
from bottle import request, template,route,run,post

@route('/')
def index():
    return template('val.html')

@post('/result')
def result():
    result=request.forms
    print(result)       #Unable to print 

    return template("result",result = result)


if __name__ == '__main__':
    run(host='localhost',port=8080,debug='True',reloader='True')