# main spider
    #.decode("unicode_escape")
import scrapy
class Demospider(scrapy.spiders.Spider):
    name="demo"
    
    start_urls=["https://tieba.baidu.com/f?ie=utf-8&kw=dnf"]
    def parse(selfself,response):
        title_cnt=0
        for x in response.xpath('//a[@class="j_th_tit "][@title]/text()'):
            print x.extract()
            title_cnt=title_cnt+1
        print "title num[%d]" %title_cnt



