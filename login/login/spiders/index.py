# -*- coding: utf-8 -*-
import scrapy
import urllib
from PIL import Image

class IndexSpider(scrapy.Spider):
    name = 'index'
    allowed_domains = ['sjtu.edu.cn']
    start_urls = ['https://src.sjtu.edu.cn/login/']
    login_url='https://src.sjtu.edu.cn/login/'
    bug_url='https://src.sjtu.edu.cn/list/?page=1'

    def parse(self, response):
        formdata={
            'username': '',
            'password': ''
        }
        captcha_0=response.xpath('//input[@name="captcha_0"]/@value').get()
        formdata['captcha_0']=captcha_0
        csrfmiddlewaretoken=response.xpath('//input[@name="csrfmiddlewaretoken"]/@value').get()
        formdata['csrfmiddlewaretoken']=csrfmiddlewaretoken
        captcha_url = response.xpath('//img/@src').get()
        captcha_url = 'https://src.sjtu.edu.cn/' + captcha_url
        #print captcha_url
        captcha = self.check_captcha(captcha_url)
        formdata['captcha_1'] = captcha
        yield scrapy.FormRequest(url=self.login_url,formdata=formdata,callback=self.parse_after_login)

    def parse_after_login(self,response):
        if response.url=="https://src.sjtu.edu.cn/":
            yield scrapy.FormRequest(self.bug_url,callback=self.parse_bug)
            print "login successful!"
        else:
            print "login failed!"


    def parse_bug(self,response):
        #print response.url
        if response.url==self.bug_url:
            print "join bug_list successful!"
            bug_list=response.xpath('//td/a[contains(@href,"/post/")]/text()').getall()
            for bug in bug_list:
                print bug.strip()
        else:
            print "join bug_list failed!"
    def check_captcha(self,image_url):
        urllib.urlretrieve(image_url,'captcha.jpg')
        image=Image.open('captcha.jpg')
        image.show()
        captcha=raw_input('please input captcha:')
        return captcha

