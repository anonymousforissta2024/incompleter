#Source: https://stackoverflow.com/questions/67668673/how-to-pick-up-the-correct-class-nameerror
import sys
import tldextract


class Scraper:
    scrapers = {}

    def __init_subclass__(scraper_class):
        Scraper.scrapers[scraper_class.url] = scraper_class # .url -> Unresolved attribute reference 'url' for class 'Scraper' 

    @classmethod
    def for_url(cls, url):
        k = tldextract.extract(url)
        return scrapers[k.domain]() #<-- Unresolved reference 'scrapers' 


class BBCScraper(Scraper):
    url = 'bbc.co.uk'

    def scrape(s):
        print(s)
        # FIXME Scrape the correct values for BBC
        return "Yay works!"


url = 'https://www.bbc.co.uk/'
scraper = Scraper.for_url(url)
scraper.scrape("yay")