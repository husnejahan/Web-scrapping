import scrapy


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # title = response.css('title::text').extract()
        # yield {'titletext': title}

        quote = response.css("div.quote")
        title = quote.css("span.text::text").extract()
        author = quote.css(".author::text").extract()
        tags = quote.css("div.tags a.tag::text").extract()
        yield {
            'title': title,
            'author': author,
            'tags': tags
        }
