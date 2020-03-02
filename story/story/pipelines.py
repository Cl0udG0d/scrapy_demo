# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class StoryPipeline(object):
    def __init__(self):
        dbparams={
            'host':'127.0.0.1',
            'port':'3306',
            'user':'root',
            'password':'root',
            'database':'story',
            'charset':'utf8'
        }
        self.conn=pymysql.connect(host="127.0.0.1", user="root",password="root",database="story",charset="utf8")
        self.cursor=self.conn.cursor()
        self._sql=None

    def process_item(self, item, spider):
        self.cursor.execute(self.sql,(item['title'],item['content']))
        self.conn.commit()
        return item

    @property
    def sql(self):
        if not self._sql:
            self._sql="""
                insert into article(title,content) values (%s,%s)
            """
            return self._sql
        return self._sql