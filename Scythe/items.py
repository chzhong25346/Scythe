# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader.processors import TakeFirst

# Enmax item
class Enmax_Item(scrapy.Item):
    # id = scrapy.Field(output_processor=TakeFirst())
    load = scrapy.Field(output_processor=TakeFirst())
    date = scrapy.Field(output_processor=TakeFirst())
    # tou = scrapy.Field(output_processor=TakeFirst())


# ShpgxLng item
class ShpgxLng_Item(scrapy.Item):
    date = scrapy.Field(output_processor=TakeFirst())
    rmb_ton = scrapy.Field(output_processor=TakeFirst())
    dollar_mmbtu = scrapy.Field(output_processor=TakeFirst())
    rmb_gj = scrapy.Field(output_processor=TakeFirst())


# PSAC item
class Psac_Item(scrapy.Item):
    aeco = scrapy.Field(output_processor=TakeFirst())
    station2 = scrapy.Field(output_processor=TakeFirst())
    dawn = scrapy.Field(output_processor=TakeFirst())
    henry_aeco_diff = scrapy.Field(output_processor=TakeFirst())
    henry = scrapy.Field(output_processor=TakeFirst())
    wti = scrapy.Field(output_processor=TakeFirst())
    wcs = scrapy.Field(output_processor=TakeFirst())
    wti_wcs_diff = scrapy.Field(output_processor=TakeFirst())
    date = scrapy.Field(output_processor=TakeFirst())
