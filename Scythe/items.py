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
    date = scrapy.Field(output_processor=TakeFirst())
    aeco = scrapy.Field(output_processor=TakeFirst())
    station2 = scrapy.Field(output_processor=TakeFirst())
    dawn = scrapy.Field(output_processor=TakeFirst())
    henry_aeco_diff = scrapy.Field(output_processor=TakeFirst())
    henry = scrapy.Field(output_processor=TakeFirst())
    wti = scrapy.Field(output_processor=TakeFirst())
    wcs = scrapy.Field(output_processor=TakeFirst())
    wti_wcs_diff = scrapy.Field(output_processor=TakeFirst())
    sp_500_energy = scrapy.Field(output_processor=TakeFirst())
    amex_oil = scrapy.Field(output_processor=TakeFirst())
    tsx_energy = scrapy.Field(output_processor=TakeFirst())
    tsx_og_producers = scrapy.Field(output_processor=TakeFirst())
    tsx_og_services = scrapy.Field(output_processor=TakeFirst())
    ca_us_ex_rate = scrapy.Field(output_processor=TakeFirst())
    tenyr_cdn_gov_bond_yield = scrapy.Field(output_processor=TakeFirst())



# BOE US Rig item
class Boe_US_rig_Item(scrapy.Item):
    date = scrapy.Field(output_processor=TakeFirst())
    total = scrapy.Field(output_processor=TakeFirst())
    oil = scrapy.Field(output_processor=TakeFirst())
    gas = scrapy.Field(output_processor=TakeFirst())
    eagle_ford = scrapy.Field(output_processor=TakeFirst())
    appalachian = scrapy.Field(output_processor=TakeFirst())
    permian = scrapy.Field(output_processor=TakeFirst())
    williston = scrapy.Field(output_processor=TakeFirst())
    dj_niobrara = scrapy.Field(output_processor=TakeFirst())
    other_basins = scrapy.Field(output_processor=TakeFirst())


# BOE CA Rig item
class Boe_CA_rig_Item(scrapy.Item):
    date = scrapy.Field(output_processor=TakeFirst())
    total = scrapy.Field(output_processor=TakeFirst())
    oil = scrapy.Field(output_processor=TakeFirst())
    gas = scrapy.Field(output_processor=TakeFirst())
    alberta = scrapy.Field(output_processor=TakeFirst())
    bc = scrapy.Field(output_processor=TakeFirst())
    saskatchewan = scrapy.Field(output_processor=TakeFirst())
    manitoba = scrapy.Field(output_processor=TakeFirst())
    other_provinces = scrapy.Field(output_processor=TakeFirst())
