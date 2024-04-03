# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals, Request

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

def get_cookies_dict():
    cook_str='ll="108310"; bid=52ZfGuQZVlY; __yadk_uid=J4F7lCBzACBtX2wLQwHHvltbmudvPLpR; _pk_id.100001.4cf6=cd133b2aaef5c608.1710233088.; _pk_ses.100001.4cf6=1; ap_v=0,6.0; __utma=30149280.40404135.1710313520.1710313520.1710313520.1; __utmb=30149280.0.10.1710313520; __utmc=30149280; __utmz=30149280.1710313520.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1336224769.1710313520.1710313520.1710313520.1; __utmb=223695111.0.10.1710313520; __utmc=223695111; __utmz=223695111.1710313520.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _vwo_uuid_v2=DFBDC5A2A26992666DF99B5AF8A602CCD|781bd21106563f349435fb594f9f3b1e; dbcl2="279013245:xEnIAYd/jXk"; ck=Hw6r; push_noty_num=0; push_doumail_num=0; frodotk_db="f7fb5884f921a0e9e7f2098eeb64e2bb"'
    cookies={}
    for item in cook_str.split(';'):
        key, value=item.split('=',maxsplit=1)
        cookies[key]=value
    return cookies

COOKIES=get_cookies_dict()

class ScrapydemoSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)


class ScrapydemoDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request: Request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # request.meta({'proxy': 'socks5://192.168.41.248:38304'}) # proxy
        request.cookies=COOKIES   # cookies
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info("Spider opened: %s" % spider.name)
