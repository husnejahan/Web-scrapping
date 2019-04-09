# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import sqlite3

# conn = sqlite3.connect('geappliance.db')
# curr= conn.cursor()
#
# curr.execute(""" create table appliance_tb (
#                  product_name text,
#                  product_codes text,
#                  product_code  text,
#                  product_price  int,
#                  product_imagelink text
#
#                  )""")
# conn.commit()
# conn.close()


class GeappliancePipeline(object):


    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = sqlite3.connector.connect("geappliance.db")
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS appliance_tb""")
        self.curr.execute("""create table appliance_tb(

                         product_name text,
                         product_codes text,
                         product_code  text,
                         product_price  int,
                         product_imagelink text
                         )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        self.curr.execute("""insert into quotes_tb values (%s,%s,%s)""", (
            items['product_name'][0],
            items['product_code'][0],
            items['product_price'][0],
            items['product_imagelink'][0]
        ))
         self.conn.commit()