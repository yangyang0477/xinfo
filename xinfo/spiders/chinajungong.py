# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from items import NewsItem


class ChinajungongSpider(CrawlSpider):
    name = 'chinajungong'
    allowed_domains = ['chinajungong.com']
    start_urls = ['http://www.chinajungong.com/News/']
    #http://www.chinajungong.com/News/201906/36518.html
    rules = (
        Rule(LinkExtractor(allow=r'News\/\d+\/\d+\.html'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
        item = NewsItem()
        item
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        yield item
