import scrapy


class RoCandeiasSpider(scrapy.Spider):
    name = 'ro_candeias'
    start_urls = ['http://www.diariomunicipal.com.br/arom']

    def parse(self, response):
        yield {"body": response.text}
