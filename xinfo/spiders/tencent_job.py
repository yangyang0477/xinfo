# -*- coding: utf-8 -*-
import scrapy
import logging
logger = logging.getLogger(__name__)

class TencentJobSpider(scrapy.Spider):
    name = 'tencent_job'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/search.html?query=ci_1']

    def parse(self, response):
        div_list = response.xpath("//div[@class ='recruit-list']")
        print(div_list)
        for div in div_list:
            item = {}
            item['title'] = div.xpath("./a/h4/text()").extract_first()
            item['position'] = div.xpath("./a/p[1]/span[2]/text()").extract_first()
            item['publish_date'] = div.xpath("./a/p[1]/span[4]/text()").extract_first()
            logger.wraning(item)
            yield item
        next_url = response.xpath("//a[@id='next']/@herf").extract_first()
        if next_url != 'javascript':
            next_url = 'http://hr.tencent.com/'+next_url
            yield scrapy.Request(
                next_url,
                callback=self.parse,
                # meta = {"item":item}
                # dont_filter = False 请求过的Url不会被过滤，一般前后采集的内容会增加的时候，dontfilter设置为false
            )
        # def parse1(self,response):
        #     response.meta["item"]
