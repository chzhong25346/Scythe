# -*- coding: utf-8 -*-
import scrapy
import json
import datetime
from scrapy.http import FormRequest
from scrapy.loader import ItemLoader
from Scythe.items import ShpgxLng_Item


class ShpgxLngSpider(scrapy.Spider):
    name = 'shpgx_lng'
    allowed_domains = ['www.shpgx.com']
    start_urls = ['https://www.shpgx.com/html/jkLNGdaj.html/']

    def start_requests(self):
        url = "https://www.shpgx.com/marketzhishu/dataList"
        headers = {"Referer": "https://www.shpgx.com/html/jkLNGdaj.html"}
        formdata = {"zhishukind": "6",
                    "area": "22",
                    "starttime":"",
                    "endtime":"",
                    "start": "0",
                    "length": "3",
                    "ts": "1589333667544"}
        yield FormRequest(url, method='POST', headers=headers, formdata=formdata)


    def parse(self, response):
        data = json.loads(response.body.decode('utf-8'))
        for i in data['root']:
            date = datetime.datetime.strptime(i['strdate'], '%Y-%m-%d')
            _PRICE = i['tradeprice'].split(',')
            rmb_ton = _PRICE[0]
            dollar_mmbtu = _PRICE[1]
            rmb_gj = _PRICE[2]
            l = ItemLoader(item=ShpgxLng_Item(), response=response)
            l.add_value('date', date)
            l.add_value('rmb_ton', rmb_ton)
            l.add_value('dollar_mmbtu', dollar_mmbtu)
            l.add_value('rmb_gj', rmb_gj)
            yield l.load_item()
