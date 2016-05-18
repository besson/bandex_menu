from scrapy.selector import Selector
from scrapy.http import Request
from bandex_menu.items import Menu
from scrapy.contrib.spiders import CrawlSpider


class BandejaoUspSpider(CrawlSpider):
    name = "bandejao_usp"
    start_urls = ["http://www.usp.br/coseas/COSEASHP/COSEAS2010_cardapio.html"]

    def parse(self, response):
        main_selector =  Selector(response)
        bandex_selectors = main_selector.xpath("//h5/a")

        for sel in bandex_selectors:
            url = sel.xpath("./@href").extract()[0]
            name = sel.xpath("./text()").extract()[0]
