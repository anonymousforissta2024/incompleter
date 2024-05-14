#Source: https://stackoverflow.com/questions/70706978/loginmanager-typeerror-nonetype-object-is-not-callable
from website import create_app

app=create_app()

if __name__=='__main__':
    app.run(host='0.0.0.0',port=80,debug=True)