# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
import re
from py_email_scraping.items import EmailItem  


class MySpider(scrapy.Spider):
    name = "marketparts"
    
    def __init__(self, domain=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.allowed_domains = [domain]
        self.start_urls = [f"http://{domain}"]

    def parse(self, response):
        # Extract emails from the response body
        emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', response.text)
        for email in emails:
            item = EmailItem()
            item['email'] = email
            yield item

        # Follow valid links
        for href in response.xpath("//a/@href").getall():
            if href.startswith(('http', 'https', '/')):
                yield response.follow(href, self.parse)

