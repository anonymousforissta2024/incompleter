#Source: https://stackoverflow.com/questions/51300845/attributeerror-module-http-server-has-no-attribute-threadinghttpserver
def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()