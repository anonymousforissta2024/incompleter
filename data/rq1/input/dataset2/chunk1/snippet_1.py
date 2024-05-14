#Source: https://stackoverflow.com/questions/48055880/attributeerror-exit-with-socketserver-on-python-3-4-3
import urllib.request
import http.server
import socketserver
PORT = 8000

def requestHandler(request, client_address,server):
    # test to print to console when the handler is invoked. 
    print("Request = " + str(request) + " Client Address = " + str(client_address) + " Server = " + str(server))

def startWebServer():
    Handler = requestHandler
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.serve_forever()

def main():
    startWebServer()

main()