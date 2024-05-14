#Source: https://stackoverflow.com/questions/31909929/webscraping-with-python3-ignoring-duplicate-attribute-errors
import requests
from xml.dom.minidom import parse, parseString


class Scraper:

    def __init__( self ):

        pass

    def list(self,pages=1):

        response = requests.get('http://example.com')

        dom = parseString(response.text)

        print(dom.toxml)


if __name__ == "__main__":

    scraper = Scraper()

    scraper.list()