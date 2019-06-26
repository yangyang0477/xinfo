# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
logger = logging.getLogger(__name__)

class XinfoPipeline(object):
    def process_item(self, item, spider):
    #判断来自哪个spider
        if spider.name == 'chiajungong':
            logger.warning('this is a test')
        # print(item)
            return item
        elif spider.name == 'tencent_job':
            return item