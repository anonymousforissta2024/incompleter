#Source: https://stackoverflow.com/questions/73739789/parsing-xml-with-python-returning-nonetype-object-not-callable-typeerror-after
from bs4 import BeautifulSoup
import argparse


with open('Sample1.xml.xml', 'r') as f:
    data = f.read()

Bs_data = BeautifulSoup(data, "xml")

findTag1 = Bs_data.findaAll('CATALOG')
findTag1Child = Bs_data.find({'COMMON': ''})
findTag1Child2 = Bs_data.find({'BOTANICAL'})




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(findTag1Child)
    print(findTag1)
    print(findTag1Child2)