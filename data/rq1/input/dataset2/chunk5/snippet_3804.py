#Source: https://stackoverflow.com/questions/61908463/scraping-website-with-python3-attributeerror-nonetype-object-has-no-attribu
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = 'https://www.bloomberg.com/quote/SPX:IND'    
page = urlopen(html)    
data = BeautifulSoup(page, 'html.parser')    
name_box = data.find('h1', attrs={'class': 'companyName__99a4824b'}) 
name = name_box.text.strip() 
print(name)