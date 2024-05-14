#Source: https://stackoverflow.com/questions/36877016/typeerror-str-does-not-support-the-buffer-interface-in-html2text
import urllib
import html2text
url='http://www.google.com'
page = urllib.request.urlopen(url)
html_content = page.read()
rendered_content = html2text.html2text(html_content)