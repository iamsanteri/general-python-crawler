import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from ..items import CompanyDataItem


class YourWebsiteSpider(CrawlSpider):
    name = "yourWebsiteSpider"
    allowed_domains = ["yourwebsite.com"]
    start_urls = [
        #'https://www.yourwebsite.com',
    ]

    rules = (
        Rule(LinkExtractor(allow=''), callback='parse_page', follow=True),
    )

    def parse_page(self, response):
        emails = response.css("body").re('([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)')
        for email_item in emails:
            extracted_email = CompanyDataItem(
                email=email_item,
            )
            yield extracted_email

# Run command: scrapy crawl yourWebsiteSpider -o desiredCSVname.csv
