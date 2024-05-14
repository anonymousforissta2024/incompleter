#Source: https://stackoverflow.com/questions/54414067/attributeerror-in-object-has-no-attribute-tohtml-pyqt5
import sys
import bs4 as bs
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEnginePage, QWebEngineView


class Page(QWebEngineView):

    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        print('Load finished')
        self.app.quit()


def main():
    page = Page('https://pythonprogramming.net/parsememcparseface/').toHtml()
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    js_test = soup.find('p', class_='jstest')
    print(js_test.text)

if __name__ == '__main__': main()