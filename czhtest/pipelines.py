# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy import signals
from scrapy.contrib.exporter import XmlItemExporter
class CzhtestPipeline(object):
    def __init__(self):
        self.files={}

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('%s_json.json' % spider.name, 'w+b')
        self.files[spider] = file
        self.exporter = XmlItemExporter(file)
        self.exporter.start_exporting()

        self.sz_file = open("sz.ps4","w+b")
        self.sz_saving = XmlItemExporter(self.sz_file)
        self.sz_saving.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        file = self.files.pop(spider)
        file.close()

        self.sz_saving.finish_exporting()
        self.sz_file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        if (item["content"][0].find(u"深圳")!=-1):
            self.sz_saving.export_item(item)
        return item
