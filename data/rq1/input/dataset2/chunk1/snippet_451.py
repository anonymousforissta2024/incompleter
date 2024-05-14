#Source: https://stackoverflow.com/questions/59110653/typeerror-bytearray-object-cannot-be-interpreted-as-an-integer
class ChunkingRequestHandler(BaseHTTPRequestHandler):
    ALWAYS_SEND_SOME = False
    ALLOW_GZIP = False
    protocol_version = 'HTTP/1.1'
    def do_GET(self):
        ae = self.headers.get('accept-encoding') or ''

        # send some headers
        self.send_response(200)
        self.send_header('Transfer-Encoding', 'chunked')
        self.send_header('Content-type', 'audio/x-wav')

        self.end_headers()

        data = bytearray(wav_header)
        data.append(bytearray(stream.read(CHUNK)))
        print(data)
        self.wfile.write(b"%X\r\n%s\r\n" % (len(data), data))

        while True:
            data = bytearray(stream.read(CHUNK))
            self.wfile.write(b"%X\r\n%s\r\n" % (len(data), data))

        # send the chunked trailer
        self.wfile.write('0\r\n\r\n')