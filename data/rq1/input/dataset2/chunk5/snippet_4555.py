#Source: https://stackoverflow.com/questions/55865296/how-do-i-get-rid-of-the-typeerror
# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each appartment
containers = page_soup.findAll("div", {"class":"list-item-container"})

filename = "asunnot.csv"
f = open(filename, "w")

headers = "Kohdetta Vuokraa, Huoneistot, Talotyyppi ja Koko, Sijainti, Vapautuu, Vuokra"

f.write(headers)
count = 0
for page in range(1,10):
    my_url = "https://www.vuokraovi.com/vuokra-asunnot/Uusimaa?page={}&pageType="
    for container in containers:

        Vuokranantaja = container.findAll("div", {"class":"hidden-xs col-sm-3 col-4"})[0].img["alt"]

        Huoneistot = container.findAll("li", {"class":"semi-bold"})[1].text

        Talotyyppi = container.findAll("li", {"class":"semi-bold"})[0].text

        Sijainti = container.findAll("div", {"class":"hidden-xs col-sm-4 col-3"})[0].findAll("span", {"class":"address"})[0].text.strip().replace("\r", "").replace("\n", "").replace(" ", "").replace(",", ", ")

        Vapautuu = container.findAll("div", {"class":"hidden-xs col-sm-4 col-3"})[0].findAll("span", {"class":"showing-lease-container hidden-xs"})[0].li.text

        Vuokra = container.findAll("li", {"class":"rent"})[0].text.strip()