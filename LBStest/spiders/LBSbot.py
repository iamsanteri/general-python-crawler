import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import TitleItem


class LBSbotSpider(CrawlSpider):
    name = "LBSbot"
    allowed_domains = ["lostbookofsales.com"]
    start_urls = [
        'https://www.lostbookofsales.com/',
    ]

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_post', follow=True),
    )

    def parse_post(self, response):
        if (response.css(".post-full-title::text").get()):
            extractedPostInfo = TitleItem(
                title=response.css(".post-full-title::text").get(),
                date=response.css(".byline-meta-date::text").get(),
            )
            return extractedPostInfo