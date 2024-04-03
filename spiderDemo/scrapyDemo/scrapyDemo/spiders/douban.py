import scrapy
from scrapy import Selector, Request
from scrapyDemo.items import MovieItem
from scrapy.http import HtmlResponse
import re

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    # way 1: get ten page()
    # start_urls = ["https://movie.douban.com/top250"]

    # way 2: get ten page()
    def start_requests(self):
        for page in range(10):
            yield  Request(url=f"https://movie.douban.com/top250?start={page*25}&filter=")

    def parse(self, response: HtmlResponse):
        sel=Selector(response)
        # list_item=sel.css('#content > div > div.article > ol > li')
        list_item=sel.xpath('//ol/li')
        
        for item in list_item:
            movie_item=MovieItem()
            # movie_item['title']=item.css('span.title::text').get()
            # movie_item['rank']=item.css('span.rating_num::text').get()
            # movie_item['subject']=item.css('span.inq::text').get()
            movie_item['title']=item.xpath(".//div[@class='hd']//span[1]/text()").get()
            movie_item['rank']=item.xpath(".//div[@class='bd']/div/span[2]/text()").get()
            movie_item['subject']=item.xpath(".//div[@class='bd']/p[2]/span/text()").get()

            url_detail=item.xpath(".//div[@class='pic']/a/@href").get()
            yield Request(url=url_detail,callback=self.parse_detail,cb_kwargs={'item': movie_item})
        
        # way 1: get ten page()
        # list_href=sel.css('div.paginator > a::attr(href)')
        # for href in list_href:
        #     yield Request(url=response.urljoin(href.get()))
            

    def parse_detail(self, response, **kwargs):
        movie_item=kwargs['item']
        sel=Selector(response)
        movie_item['duration']=sel.xpath("//span[@property='v:runtime']/text()").get()
        
        intro=sel.xpath("//span[@property='v:summary']/text()").get()
        intro_clear=re.sub(r'[\s\r\n]','',intro)
        movie_item['intro']=intro_clear
        yield movie_item
