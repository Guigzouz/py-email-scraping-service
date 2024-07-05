# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import re
from py_email_scraping.items import EmailItem  

class MySpider(scrapy.Spider):
    name = "marketparts"
    allowed_domains = ["marketparts.com"]
    start_urls = [
        "https://www.marketparts.com/"
    ]

    def parse(self, response):
        # Extract emails from the response body
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text)
        for email in emails:
            item = EmailItem()
            item['email'] = email
            yield item

        # Follow valid links
        for href in response.xpath("//a/@href").getall():
            # Skip links that don't start with http, https, or /
            if href.startswith(('http', 'https', '/')):
                yield response.follow(href, self.parse)
