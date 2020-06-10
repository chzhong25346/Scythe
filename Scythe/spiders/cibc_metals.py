# -*- coding: utf-8 -*-
import scrapy
import datetime
import re
from urllib.parse import urljoin
from Scythe.items import CIBC_metals_Item
from scrapy.http import Request
from scrapy.loader import ItemLoader

class CibcMetalsSpider(scrapy.Spider):
    name = 'cibc_metals'
    allowed_domains = ['www.preciousmetals.cibc.com']
    start_urls = ['https://www.preciousmetals.cibc.com/']
    gbar_1oz_url = urljoin(start_urls[0], 'gold-GB1Ecom.aspx')
    gcoin_1oz_url = urljoin(start_urls[0], '3bd09c35-a09d-4feb-bb55-0076ac8692fa.aspx')
    sbar_100oz_url = urljoin(start_urls[0], '72607555-cf7d-46c8-9587-40d42f31c0b1.aspx')
    scoin_1oz_url = urljoin(start_urls[0], 'e084941a-39ec-4a44-9c5d-5b9c55cd5ae7.aspx')
    items = {}

    def parse(self, response):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.items['date'] = date
        yield Request(self.gbar_1oz_url, meta=self.items, callback=self.parse_gbar_1oz)


    def parse_gbar_1oz(self, response):
        price = self.parse_price(response)
        # self.items['gbar_1oz'] = price
        self.items['gbar_1oz'] = price
        yield Request(self.gcoin_1oz_url, meta=self.items, callback=self.parse_gcoin_1oz)

    def parse_gcoin_1oz(self, response):
        price = self.parse_price(response)
        self.items['gcoin_1oz'] = price
        yield Request(self.sbar_100oz_url, meta=self.items, callback=self.parse_sbar_100oz)

    def parse_sbar_100oz(self, response):
        price = self.parse_price(response)
        self.items['sbar_100oz'] = price
        yield Request(self.scoin_1oz_url, meta=self.items, callback=self.parse_scoin_1oz)

    def parse_scoin_1oz(self, response):
        price = self.parse_price(response)

        l = ItemLoader(item=CIBC_metals_Item(), response=response)
        l.add_value('date', response.meta.get('date'))
        l.add_value('gbar_1oz', response.meta.get('gbar_1oz'))
        l.add_value('gcoin_1oz', response.meta.get('gcoin_1oz'))
        l.add_value('sbar_100oz', response.meta.get('sbar_100oz'))
        l.add_value('scoin_1oz', price)
        return l.load_item()

    def parse_price(self, response):
        price = response.xpath('//span[@id="ctl00_ContentRegion_Price"]/text()').extract_first()
        price = re.sub('[,$,CAD, ]', '', price)
        return price
