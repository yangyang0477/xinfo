# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import time

class ChinajungongSpider(CrawlSpider):
    name = 'chinajungong'
    allowed_domains = ['chinajungong.com']
    start_urls = ['http://www.chinajungong.com/News/']
    rules = (
        Rule(LinkExtractor(allow=r'News\/\d+\/\d+\.html'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        item['title'] = response.xpath("//div[@class = 'mainnew_l']//h1/text()").extract()
        item['news_date'] = response.xpath("//span[@class = 'news_info_time']/text()").extract()  # 发布时间
        item['content'] = response.xpath("//div[@class = 'news_info_content']//text()").extract()# 正文
        item['news_url'] = response.url  # url
        item['crawl_date'] = time.strftime('%Y-%m-%d')
        item['referer_web'] = response.xpath("//span[@class='news_info_from']/text()").extract() # 引用的网站名
        item['source'] = 'chinajungong.com'  # 来源网站(网易科技)
        yield item
        #print(title,news_date,news_url,crawl_date,content,referer_web)
