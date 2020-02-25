# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os
import urllib
from scrapy.pipelines.images import ImagesPipeline
import settings
i=1
class BuxiusePipeline(object):
    def __init__(self):
        self.path=os.path.join(os.path.dirname(os.path.dirname(__file__)),'images')
        if not os.path.exists(self.path):
            os.mkdir(self.path)

    def process_item(self, item, spider):
        global i
        link_list=item['image_urls']
        for link in link_list:
            print i
            image_name=str(i)+".jpg"
            urllib.urlretrieve(link,os.path.join(self.path,image_name))
            i=i+1
        return item

# class BuxiuseImagesPipeline(ImagesPipeline):
#     def file_path(self, request, response=None, info=None):
#         global i
#         i=i+1
#         return str(i)+".jpg"

