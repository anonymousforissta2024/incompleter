#Source: https://stackoverflow.com/questions/58236685/request-headers-gives-typeerror-environheaders-object-is-not-callable
@app.route('/auth', methods=['GET'])
def auth():
    return request.headers.get('x-authorization')