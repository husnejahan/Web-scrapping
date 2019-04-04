# -*- coding: utf-8 -*-
import scrapy
from ..items import AmazontutorialItem

class AmazonSpiderSpider(scrapy.Spider):
    name = 'amazon'
    start_urls = [
        'https://www.amazon.com/s/ref=lp_283155_nr_p_n_publication_date_0?fst=as%3Aoff&rh=n%3A283155%2Cp_n_publication_date%3A1250226011&bbn=283155&ie=UTF8&qid=1550908246&rnid=1250225011'
    ]

    def parse(self, response):
        items = AmazontutorialItem()

        product_name = response.css('.s-access-title::text').extract()
        product_author = response.css('.a-color-secondary+ .a-color-secondary , #result_0 .a-color-secondary .a-text-normal').css('::text').extract()
        product_price = response.css('.a-spacing-none:nth-child(2) .sx-price-fractional , .a-spacing-none:nth-child(2) .sx-price-whole').css('::text').extract()
        product_imagelink = response.css('.cfMarker::attr(src)').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items
		
