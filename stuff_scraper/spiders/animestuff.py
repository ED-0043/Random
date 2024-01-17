from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.loader import ItemLoader
from ..items import StuffItem


class AnimestuffSpider(CrawlSpider):
    name = "animestuff"
    allowed_domains = ["animepahe.ru"]
    start_urls = ["https://animepahe.ru"]

    rule = Rule(LinkExtractor(allow_domains=(r'anime')), callback='parse_item')

    def parse_item(self, response):
        # yield{
        #     'name': response.css('').get(),
        #     'title': response.css('').get(),
        #     'rank': response.css('').get(),
        #     'score': response.css('').get(),
        # }
        pass
    