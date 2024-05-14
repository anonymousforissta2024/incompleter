#Source: https://stackoverflow.com/questions/69848907/beautifulsoup-attributeerror-nonetype-object-has-no-attribute-text
res = requests.get('https://www.babynamesdirect.com/baby-names/indian/boy/trending')
soup = BeautifulSoup(res.text, 'html5lib')
ul  = soup.find('div', class_ = 'ntb boy').find_all('li')
names = [name.dt.text for name in ul]
print(names)