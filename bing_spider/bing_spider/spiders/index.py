# -*- coding: utf-8 -*-
import scrapy
import time

class IndexSpider(scrapy.Spider):
    page=1
    name = 'index'
    allowed_domains = ['bing.com']
    start_urls = ['']
    base_domain="https://cn.bing.com/"
    def parse(self, response):
        time.sleep(10)
        url_list=response.xpath('//h2/a[@target="_blank"]/@href').extract()
        print "Now write: " + str(self.page)
        self.page += 1
        f = open('sql_bug2.txt', 'a+')
        for url in url_list:
            f.write(url + '\n')
        f.close()
        time.sleep(5)
        next_url=response.xpath('//a[@class="sb_pagN sb_pagN_bp b_widePag sb_bp "]/@href').get()
        if not next_url:
            print "don't find next_url"
            return
        else:
            next_url = self.base_domain + next_url
            yield scrapy.Request(next_url)