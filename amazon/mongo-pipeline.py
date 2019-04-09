# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> Item Containers -> Json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo database

import pymongo


class QuotetutorialPipeline(object):

    def __init__(self):
        connection = pymongo.MongoClient(
            'localhost',
            27017
        )
        db = connection["myquotes"]
        self.collection = db["quotes_tb"]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
