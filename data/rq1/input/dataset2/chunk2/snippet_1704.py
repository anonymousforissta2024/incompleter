#Source: https://stackoverflow.com/questions/41754786/nameerror-name-qwebpage-is-not-defined
import sys  
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
from PyQt5.QtWebEngineWidgets import *  
from lxml import html 

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  

  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

url = 'http://pycoders.com/archive/'  
r = Render(url)  
result = r.frame.toHtml()
#This step is important.Converting QString to Ascii for lxml to process
archive_links = html.fromstring(str(result.toAscii()))
print(archive_links)