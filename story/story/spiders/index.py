# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from story.items import StoryItem

class IndexSpider(CrawlSpider):
    name = 'index'
    allowed_domains = ['biquge.com.cn']
    start_urls = ['http://biquge.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.biquge.com.cn/[a-z]+/',deny='.*.html'), follow=True),
        Rule(LinkExtractor(allow=r'https://www.biquge.com.cn/book/\d+/',deny='.*.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # print response.url
        title=response.xpath('//div[@id="info"]/h1/text()').get()
        content=response.xpath('//div[@id="intro"]/text()').get()
        print(title)
        print(content)
        item=StoryItem(title=title,content=content)
        yield item

