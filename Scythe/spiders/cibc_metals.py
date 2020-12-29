# -*- coding: utf-8 -*-
import scrapy
import datetime
import re
import json
from urllib.parse import urljoin
from Scythe.items import CIBC_metals_Item
from scrapy.http import Request, FormRequest
from scrapy.loader import ItemLoader

class CibcMetalsSpider(scrapy.Spider):
    name = 'cibc_metals'
    allowed_domains = ['www.preciousmetals.cibc.com']
    start_urls = ['https://www.preciousmetals.cibc.com/']
    gbar_1oz_url = urljoin(start_urls[0], 'ItemSelection/GetItems/Ecom_Gold/0/10/Popularity')
    gcoin_1oz_url = urljoin(start_urls[0], 'ItemSelection/GetItems/Ecom_Gold/0/10/Popularity')
    sbar_100oz_url = urljoin(start_urls[0], 'ItemSelection/GetItems/Ecom_Silver/0/10/Popularity')
    scoin_1oz_url = urljoin(start_urls[0], 'ItemSelection/GetItems/Ecom_Silver/0/10/Popularity')
    items = {}

    def parse(self, response):
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.items['date'] = date
        yield FormRequest(url=self.gbar_1oz_url, method='GET', meta=self.items, callback=self.parse_gbar_1oz)


    def parse_gbar_1oz(self, response):
        price = self.parse_price(response, pname='1 oz Gold Bar')
        self.items['gbar_1oz'] = price
        yield FormRequest(self.gcoin_1oz_url, method='GET', meta=self.items, dont_filter=True, callback=self.parse_gcoin_1oz)


    def parse_gcoin_1oz(self, response):
        price = self.parse_price(response, pname='1 oz Gold Maple Leaf Coin (Random Year)')
        self.items['gcoin_1oz'] = price
        yield FormRequest(self.sbar_100oz_url, method='GET', meta=self.items, dont_filter=True, callback=self.parse_sbar_100oz)


    def parse_sbar_100oz(self, response):
        price = self.parse_price(response, pname='100 oz Silver Bar (RCM)')
        self.items['sbar_100oz'] = price
        yield FormRequest(self.scoin_1oz_url, method='GET', meta=self.items, dont_filter=True, callback=self.parse_scoin_1oz)


    def parse_scoin_1oz(self, response):
        price = self.parse_price(response, pname='Silver Maple Leaf Coin (Random Year)')
        l = ItemLoader(item=CIBC_metals_Item(), response=response)
        l.add_value('date', response.meta.get('date'))
        l.add_value('gbar_1oz', response.meta.get('gbar_1oz'))
        l.add_value('gcoin_1oz', response.meta.get('gcoin_1oz'))
        l.add_value('sbar_100oz', response.meta.get('sbar_100oz'))
        l.add_value('scoin_1oz', price)
        return l.load_item()


    def parse_price(self, response, pname):
        # price = response.xpath('//span[@id="ctl00_ContentRegion_Pric"]/text()').extract_first()
        # price = re.sub('[,$,CAD, ]', '', price)
        data = json.loads(response.body.decode('utf-8'))
        for i in data:
            if i['Name'] == pname:
                return i['Price']
