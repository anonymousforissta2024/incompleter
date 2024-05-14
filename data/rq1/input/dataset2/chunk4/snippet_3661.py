#Source: https://stackoverflow.com/questions/58754833/im-getting-name-error-when-running-this-code
import requests
from bs4 import BeautifulSoup as bs

session = request.session()

def get_sizes_in_stock():
    global session
    endpoint = "https://www.off---white.com/en/SE/men/products/omia065r208000010100#"
    response = session.get(endpoint)

    soup = bs(response.text,"html.parser")

    ul = soup.find("ul",{"class":"styled-radio"})
    all_sizes = ul.find_all("li")

    sizes_in_stock = []
    for size in all_sizes:
        if "availability not_on_sale" not in size["class"]:
            size_id = size["id"]
            sizes_in_stock.append(size_id.split("_")[1])

    return sizes_in_stock

print(get_sizes_in_stock())