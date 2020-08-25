# -*- coding: utf-8 -*-
import scrapy
import time
import re
from xinfo.items import NewsItem
import logging
logger = logging.getLogger(__name__)


class DarpaSpider(scrapy.Spider):
    name = 'darpa'
    allowed_domains = ['darpa.mil']
    start_urls = ['https://www.darpa.mil/news']

    def parse(self, response):
        div_list = response.xpath(
            "//div[@class = 'listing__item  has-thumbnail']")
        for div in div_list:
            item = NewsItem()
            item['title'] = div.xpath(
                "./div[@class = 'listing__right']/h2/a/text()").extract_first()
            item['news_date'] = div.xpath(
                "./div[@class = 'listing__right']/div[@class = 'listing__date']/text()").extract_first()
            item['abstract'] = div.xpath(
                "./div[@class = 'listing__right']/div[@class = 'listing__copy']/text()").extract_first()
            item['news_url'] = div.xpath(
                "./div[@class = 'listing__right']/h2/a/@href").extract_first()  # url
            item['news_url'] = 'https://www.darpa.mil' + item['news_url']
            item['crawl_date'] = time.strftime('%Y-%m-%d')
            item['source'] = 'darpa.mil'
            yield scrapy.Request(
                item['news_url'],
                callback=self.parse_detail,
                meta={'item': item}
            )
        next_url = response.xpath(
            "//a[@class = 'more-link last']/@href").extract_first()
        # 获取最后一页地址
        number = int(re.findall('news\?PP=(\d+)', next_url)[0])
        for i in range(number+1):
            yield scrapy.Request(
                'https://www.darpa.mil/' + 'news?PP={}'.format(i),
                callback=self.parse
            )

    def parse_detail(self, response):
        item = response.meta["item"]
        item['sub_title'] = response.xpath(
            "//h2[@class = 'detail__newssubtitle']/text()").extract_first()
        item['author'] = response.xpath(
            "//div[@class = 'detail__position-office']/text()").extract_first()
        item['tags'] = response.xpath(
            "//a[@class = 'listing__tag-item listing__tag-link']/text()").extract()
        item['content'] = response.xpath(
            "//div[@class = 'detail__body']//p/text()").extract()
        item['pic'] = response.xpath(
            "//div[@class = 'detail__image']//img/@src").extract()
        yield item
