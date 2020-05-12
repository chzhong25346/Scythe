# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst

# class ScytheItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

# Enmax item
class Enmax_Item(scrapy.Item):
    # id = scrapy.Field(output_processor=TakeFirst())
    load = scrapy.Field(output_processor=TakeFirst())
    date = scrapy.Field(output_processor=TakeFirst())
    # tou = scrapy.Field(output_processor=TakeFirst())
