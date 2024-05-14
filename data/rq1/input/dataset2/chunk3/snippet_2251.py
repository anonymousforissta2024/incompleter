#Source: https://stackoverflow.com/questions/64846589/attributeerror-response-content-isnt-text-what-is-the-problem
import scrapy
import json


class BasisMembersSpider(scrapy.Spider):
    name = 'basis'
    allowed_domains = ['www.basis.org.bd']

    def start_requests(self):
        start_url = 'https://basis.org.bd/get-member-list?page=1&team='
        yield scrapy.Request(url=start_url, callback=self.get_membership_no)

    def get_membership_no(self, response):

        data_array = json.loads(response.body)['data']
        next_page = json.loads(response.body)['links']['next']
        
        for data in data_array:
            next_url = 'https://basis.org.bd/get-company-profile/{0}'.format(data['membership_no'])
            yield scrapy.Request(url=next_url, callback=self.parse)
            
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.get_membership_no)

    def parse(self, response):
        print("Printing informations....................................................")