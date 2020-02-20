# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from wxapp.items import WxappItem

class IndexSpider(CrawlSpider):
    name = 'index'
    allowed_domains = ['wxapp-union.com']
    start_urls = ['http://www.wxapp-union.com/portal.php?mod=list&catid=2&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'.+list&catid=2&page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'.+article-.+\.html'), callback='parse_detail', follow=False),
    )

    def parse_detail(self, response):
        title=response.xpath('//h1[@class="ph"]/text()').get()
        author_name=response.xpath('//p[@class="authors"]/a/text()').get()
        author_time=response.xpath('//p[@class="authors"]/span/text()').get()
        article_content=response.xpath('//td[@id="article_content"]//text()').getall()
        article_content="".join(article_content).strip()
        print title
        item=WxappItem(title=title,author_name=author_name,author_time=author_time,article_content=article_content)
        yield item