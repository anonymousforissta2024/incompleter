#Source: https://stackoverflow.com/questions/69302989/web-scraping-typeerror-nonetype-object-is-not-subscriptable-how-to
my_url = str1
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")

data = page_soup.findAll("div", {"class": "_2kHMtA"})