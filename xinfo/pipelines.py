# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
#from pymongo import MongoClient
from xinfo.items import NewsItem


class XinfoPipeline(object):
    # def open_spider(self, spider):
    #     mongo_host = spider.settings.get('MONGO_HOST')
    #     client = MongoClient(mongo_host)
    #     self.collection = client['xinfo']['chinajungong']

    def process_item(self, item, spider):
        # 判断来自哪个spider
        if spider.name == 'chiajungong':
            # 判断item的类型
            if isinstance(item, NewsItem):
                #logger.warning('this is a test')
                # 强制类型转换，因为这里的item是NewsItem类
                #self.collection.insert(dict(item))
                print(item['title'])
        #    return item
        elif spider.name == 'darpa':
            #主要处理publish_date,abstract,content内容
            if isinstance(item, NewsItem):
                for i in range(len(item['pic'])):
                    item['pic'][i] = 'https://www.darpa.mil' + item['pic'][i]
                item['content'] = '\n'.join(item['content'])

                print(item['content'])

    # def close_spider(self, spider):
    #     pass
