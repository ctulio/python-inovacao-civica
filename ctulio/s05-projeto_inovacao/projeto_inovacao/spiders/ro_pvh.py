import scrapy


class RoPortoVelhoSpider(scrapy.Spider):
    name = 'ro_pvh'
    start_urls = ['http://www.diariomunicipal.com.br/arom']

    def parse(self, response):
        yield {"body": response.text}
