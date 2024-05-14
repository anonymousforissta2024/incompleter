#Source: https://stackoverflow.com/questions/71067529/beautiful-soup-attributeerror-nonetype-object-has-no-attribute-get-text
with open('source.html') as f:
   soup = BeautifulSoup(f.read(), "html.parser")

# Extract script and style elements
for s in soup(["script", "style"]):
    s.extract()

tr = soup.find_all("tr")
for t in tr:
    location = t.find('span', itemprop='name').get_text() # ERROR