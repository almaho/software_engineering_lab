import scrapy


class IsnaSpider(scrapy.Spider):
    name = 'Isna'
    allowed_domains = ['www.isna.ir']
    start_urls = ['http://www.isna.ir/']

    def parse(self, response):
        pass
