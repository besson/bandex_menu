from scrapy.selector import Selector
from scrapy.http import Request
from bandex_menu.items import Menu
from scrapy.contrib.spiders import CrawlSpider


class BandejaoUspSpider(CrawlSpider):
    name = "bandejao_usp"
    start_urls = ["http://www.usp.br/coseas/COSEASHP/COSEAS2010_cardapio.html"]

    def parse(self, response):
        sel =  Selector(response)
        urls_restaurantes = sel.xpath("//h5/a/@href").extract()

        print(urls_restaurantes)
