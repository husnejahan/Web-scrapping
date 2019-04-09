# -*- coding: utf-8 -*-
import scrapy
from ..items import GeapplianceItem


class GeapplianceSpiderSpider(scrapy.Spider):
    name = 'geappliance_spider'

    start_urls = ['https://products.geappliances.com/appliance/gea-category/refrigerators?TYPE=French+Door']

    def parse(self, response):

        items = GeapplianceItem()

        product_name = response.css('.product-title a::text').extract()
        product_codes = response.css('.product-title a::attr(href)').extract()
        product_code=[i.strip('/appliance/gea-specs/') for i in  product_codes]

        product_price = response.css('.bold-price ::text').extract()
        product_imagelink = response.css('#results-list-container img ::attr(src)').extract()


        items['product_name'] = product_name
        items['product_code'] = product_code
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink


        yield items

