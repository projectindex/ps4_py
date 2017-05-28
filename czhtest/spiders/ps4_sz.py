# main spider
import scrapy
from scrapy.contrib.loader import ItemLoader
from czhtest.items import CzhtestItem

class Demospider(scrapy.spiders.Spider):
    name="ps4"
    
    start_urls=["https://tieba.baidu.com/p/5096889787?pn=1"]
    url_base="https://tieba.baidu.com/p/5096889787?pn="
    page_cnt=176
    page_cur=1;
    def parse(self,response):
        title_cnt=0
        for node in response.xpath('//div[starts-with(@id,"post_content")]'):
            title_cnt = title_cnt + 1
            content_str="";
            for tmp in node.xpath('./div[@class="post_bubble_middle"]/text()|text()'):
                content_str=content_str+tmp.extract()
            l = ItemLoader(item=CzhtestItem(), response=response)
            l.add_value('url',response.url)
            l.add_value('level', str(title_cnt))
            l.add_value('content',content_str)
            l.add_value('comment',"mdzz")
            yield l.load_item()

        if (self.page_cur<self.page_cnt):
            self.page_cur=self.page_cur+1;
            yield scrapy.Request(self.url_base+str(self.page_cur),callback=self.parse)



