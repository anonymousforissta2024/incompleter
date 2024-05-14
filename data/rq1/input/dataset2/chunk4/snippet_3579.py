#Source: https://stackoverflow.com/questions/37761063/python-str-typeerror-str-object-is-not-callable-the-stop-code
soup = BeautifulSoup(r.content, "lxml")

berat = soup.find_all("dd", {"class": "pull-left m-0 border-none"})[0].text
var1 = str(berat)
str = string.maketrans('us', '12')
result = var1.translate(str)
print (result)