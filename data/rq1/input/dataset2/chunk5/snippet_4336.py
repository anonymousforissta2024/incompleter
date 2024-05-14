#Source: https://stackoverflow.com/questions/73379445/cant-loop-in-nested-dictionary-typeerror-argument-of-type-bool-is-not-iter
import scrapy
    
class MlSpider(scrapy.Spider):
    name = 'detalhador'
    

start_urls=['https://produto.mercadolivre.com.br/MLB-1304118411-sandalia-feminina-anabela-confortavel-pingente-mac-cod-133-_JM?attributes=COLOR_SECONDARY_COLOR%3AUHJldGE%3D%2CSIZE%3AMzU%3D&quantity=1']

def parse(self, response,**kwargs):
    import json

    d = response.xpath('//script[contains(., "window.__PRELOADED_STATE__")]/text()').re_first(r'(?s)window.__PRELOADED_STATE__ = (.+?\});')
    data = json.loads(d)
    
    temp='itemPrice'
    res = [val[temp] for key, val in data.items() if temp in val]