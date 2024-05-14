#Source: https://stackoverflow.com/questions/13175253/python-error-type-error-post-data-should-be-bytes-also-user-agent-issue
import urllib.parse
import urllib.request

url = 'http://getliberty.org/contact-us/'
user_agent = 'Mozilla/5.0 (compatible; Chrome/22.0.1229.94; Windows NT)'
values = {'Your Name' : 'Horatio',
          'Your Email' : '6765Minus4181@gmail.com',
          'Subject' : 'Hello',
          'Your Message' : 'Cheers'}

headers = {'User-Agent': user_agent }

data = urllib.parse.urlencode(values)
req = urllib.request.Request(url, data)
response = urllib.request.urlopen(req)
the_page = response.read()