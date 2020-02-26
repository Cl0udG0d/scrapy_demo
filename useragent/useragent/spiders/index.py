# -*- coding: utf-8 -*-
import scrapy
import json

class IndexSpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/user-agent']

    def parse(self, response):
        user_agent=json.loads(response.text)['user-agent']
        print user_agent
        yield scrapy.Request(self.start_urls[0],dont_filter=True)