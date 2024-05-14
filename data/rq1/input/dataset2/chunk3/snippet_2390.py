#Source: https://stackoverflow.com/questions/56149932/typeerror-in-xmlrpc-client
class HTTPSDigestAuthTransport:

    def request(self, host, handler, request_body, verbose=0):
        api_url = Setup.get_api_url()
        username = Setup.get_api_username()
        password = Setup.get_api_password()
        h = httplib2.Http()
        if verbose:
            h.debuglevel = 1
        h.add_credentials(username, password)
        h.disable_ssl_certificate_validation = True
        resp, content = h.request("https://" + api_url, "POST", body=request_body,
                              headers={'content-type': 'text/xml'})
        if resp.status != 200:
            raise ProtocolError("https://" + api_url, resp.status, resp.reason, None)
        p, u = getparser(0)
        p.feed(content)


# transport factory instance
transport = HTTPSDigestAuthTransport()

# url composition
url = "https://" + Setup.get_api_username() + ":" + Setup.get_api_password() + "@" + Setup.get_api_url()

# create the proxy
proxy = xmlrpc.client.ServerProxy(url, transport)
res = proxy.do_some_work()