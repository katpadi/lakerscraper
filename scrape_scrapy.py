"""
This is on top of the BaseSpider class.

Assumption:
    http://doc.scrapy.org/en/latest/topics/ubuntu.html#topics-ubuntu

How to run:
    scrapy runspider myspider.py
"""
from __future__ import print_function
from scrapy.item import Item, Field
from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from scrapy.http import HtmlResponse

class LakersItem(Item):
    # Items are defined in a declarative style. If you attempt to store a field
    # not defined here, an exception will be raised.
    title = Field()
    content = Field()
    url = Field()

"""
This spider crawls http://www.nba.com/schedules/intl.html?RID=26&cName=Philippines#Lakers
"""
class MySpider(BaseSpider):
    # The name is the unique identifier for this spider.
    name = 'myspider'
    # These URLs are the initial requests performed by the spider.
    start_urls = [
        'http://www.nba.com/schedules/intl.html?RID=26&cName=Philippines#Lakers'
    ]

    # The default callback for the start urls is `parse`.
    # This method must return either items or requests.
    def parse(self, response):
        s = Selector(response)
        # Instance selector
        scheds = s.xpath('//table/tr/td/span').extract()
        for sched in scheds:
            print (sched)

        # Instance selector
        sel = Selector(response)
        # Instance our item.
        item = LakersItem()

        item['title'] = sel.xpath('//h2/text()').extract()[0]
        item['url'] = response.url
        # Finally return the scraped item.
        return item
