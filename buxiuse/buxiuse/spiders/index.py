# -*- coding: utf-8 -*-
import scrapy
from buxiuse.items import BuxiuseItem

class IndexSpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['buxiuse.com']
    start_urls = ['https://www.buxiuse.com/?page=1']
    base_domain="https://www.buxiuse.com"

    def parse(self, response):
        image_urls=response.xpath('//ul[@class="thumbnails"]/li//img/@src').getall()
        next_url=response.xpath('//li[@class="next next_page"]/a/@href').get()
        item=BuxiuseItem(image_urls=image_urls)
        yield item
        if not next_url:
            return
        else:
            yield scrapy.Request(self.base_domain+next_url)
