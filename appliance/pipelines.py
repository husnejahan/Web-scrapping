# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# Scraped data -> Item Containers -> Json/csv files
# Scraped data -> Item Containers -> Pipeline -> SQL/Mongo database

import mysql.connector


class GeappliancePipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='    ',
            database='geappliance'
        )
        self.curr = self.conn.cursor()


    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS appliance_tb(""")
        self.curr.execute("""create table appliance_tb(

                                 product_name text,
                                 product_code  text,
                                 product_price  text,
                                 product_imagelink text
                                 )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into appliance_tb( values (%s,%s,%s,%s)""", (
            items['product_name'][0],
            items['product_code'][0],
            items['product_price'][0],
            items['product_imagelink'][0]
        ))
        self.conn.commit()
