#Source: https://stackoverflow.com/questions/39755313/type-error-in-python-3-5-2
import io
env['wsgi.input']        = io.StringIO(self.request_data)