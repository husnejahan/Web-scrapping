# Default structure of Scrapy projects:
(https://doc.scrapy.org/en/latest/topics/commands.html)

scrapy.cfg

myproject/

    __init__.py
    
    items.py
    
    middlewares.py
    
    pipelines.py
    
    settings.py
    
    spiders/
    
        __init__.py
        
        spider1.py
        
        spider2.py
        ...
        

# Web-scrapping
In the pycharm terminal:

scrapy crawl quotes

# storing data in item containers

scrapy crawl quotes -o items.csv

scrapy crawl name_spider -o data.csv -t csv


# To create a scrapy project

In the pycharm terminal:

scrapy startproject projectname

scrapy genspider example example.com

scrapy genspider amazon_spider  amazon.com

# CSS Selector gadget chrome

To download for chrome:

https://chrome.google.com/webstore/detail/selectorgadget/mhjhnkcfbdhnjickkkdbjoemdmbfginb

After activating selector gadget, We can select specific field,use left click to avoid unnecessary field.
