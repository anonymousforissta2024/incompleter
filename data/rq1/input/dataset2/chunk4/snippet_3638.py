#Source: https://stackoverflow.com/questions/38626868/in-python-using-amazon-bottlenose-api-i-have-nameerror
import bottlenose
from bs4 import BeautifulSoup


def item_search(keywords, search_index="Toys", item_page= 1):
    response = amazon.ItemSearch(SearchIndex=search_index, Keywords=keywords, ItemPage=item_page, ResponseGroup="Large")
    soup = BeautifulSoup(response, 'lxml')
    return soup.find('item')

def item_Lookup(item_id):
    response = amazon.ItemLookup(ItemId= item_id,  ResponseGroup="Images")
    soup = BeautifulSoup(response, 'lxml')
    return soup.find('largeimage')

def amazon_api():
    api_id = 'your api_id'
    api_key = 'your api_key'
    tag_id = 'your tag_id'

    amazon = bottlenose.Amazon(api_id,api_key,tag_id)    
    item = item_search('nike', search_index="All", item_page= 1)
    asin = item.find('asin').text

    print(asin)
    img = item_Lookup(asin)
    print(img)

amazon_api()