#Source: https://stackoverflow.com/questions/55012786/typeerror-close-spider-missing-1-required-positional-argument-reason
import scrapy
import scrapy_splash
from scrapy.linkextractors import LinkExtractor
from cointelegraph_spider.items import CointelegraphSpiderItem
import sqlite3 as sq3

class CointelegraphspiderSpider(scrapy.Spider):
    name = 'cointelegraphspider'
    allowed_domains = ['cointelegraph.com']
    start_urls = ['http://cointelegraph.com/']



    def start_requests(self):

        """
        Doc string
        """

        # Execute the LUA script for "Load Mor" button
        script = """

            function main(splash, args)
                assert(splash:go(args.url))
                splash:wait(0.5)
                local num_clicks = 2
                local delay = 1.5
                local load_more = splash:jsfunc(
                            [[
                                function ()
                                {
                                    var el = document.getElementsByClassName('post-preview-list-navigation__btn post-preview-list-navigation__btn_load-more');
                                    el[0].click();
                                } 
                            ]]

                            )

                for _ = 1, num_clicks do
                    load_more()
                    splash:wait(delay)
                end        

                return 
                {
                    html = splash:html(),
                }
            end

        """

        for url in self.start_urls:

            yield scrapy_splash.SplashRequest(
                    url=url,
                    callback=self.parse_main_page,
                    args={
                            'wait':3,
                            'lua_source':script,
                            #'timeout': 3600 # Here the max-timeout is 60 -- to increase it launch the docker with --max-timeout xxxxx
                            },
                    endpoint="execute",
                    )

    def parse_main_page(self, response):
        """
        Doc string
        """        
        # Convert Splash response into html response object
        html = scrapy.Selector(response)

        # Check DB for existing records
        conn = sq3.connect("D:\\DCC\\Projects\\crypto_projects\\master_data.db")
        db_links = conn.execute("select link from cointelegraph").fetchall() # list of tuples
        db_links = [elem[0] for elem in db_links] # flattening list
        print("DB LINKS! ", db_links)
        #db_links = ["aaa",]
        conn.close() # close connection

        # Extract all links to be followed
        news_links = LinkExtractor(restrict_xpaths=['//ul[@class="post-preview-list-cards"]/li/div/article/a', # Main Body
                                                    '//div[@class="main-news-tabs__wrp"]/ul/li/div/a'] # "Editor's Choice" & "Hot Stories"
                                    ).extract_links(html.response)

        for link in news_links[:2]:
            # Follow only new links
            if link.url not in db_links:
                yield scrapy.Request(link.url, callback=self.parse_article)


    def parse_article(self, response):
        """
        Doc string
        """

        # Create Item for Pipeline
        item = CointelegraphSpiderItem()

        item['author'] = response.xpath('//div[@class="name"]/a/text()').extract_first().strip()
        item['timestamp'] = response.xpath('//div/@datetime').extract_first().split('t')[0] # %Y-%m-%d
        item['title'] = response.xpath('//h1[@class="header"]/text()').extract_first().strip()
        item['body'] = ' '.join(response.xpath('//div[@class="post-full-text contents js-post-full-text"]/p//text()').extract())
        item['quotes'] = ';;;'.join(response.xpath('//div[@class="post-full-text contents js-post-full-text"]/blockquote//text()').extract())
        item['int_links'] = ';;;'.join(response.xpath('//div[@class="post-full-text contents js-post-full-text"]/p/a/@href').extract())
        _tmp = [elem.replace('#','') for elem in response.xpath('//div[@class="tags"]/ul/li/a/text()').extract()]
        item['tags'] = ';;;'.join([elem.replace(' ','') for elem in _tmp])
        item['link'] = response.url
        item['news_id'] = str(hash(item['link']))

        yield item