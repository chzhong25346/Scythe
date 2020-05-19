# -*- coding: utf-8 -*-
import scrapy
import json
import datetime
from scrapy.http import Request
from scrapy.loader import ItemLoader
from Scythe.items import Boe_US_rig_Item, Boe_CA_rig_Item


class BoeSpider(scrapy.Spider):
    name = 'boe'
    allowed_domains = ['boereport.com']
    start_urls = ['https://boereport.com/']
    us_rig_count = start_urls[0] + 'us-rig-count/'
    ca_rig_count = start_urls[0] + 'canada-rig-count/'

    def parse(self, response):
        us_rig_request_url = 'https://boereport.com/charts/data/chart.php?chartid=usRigCount'
        ca_rig_request_url = "https://boereport.com/charts/data/chart.php?chartid=canRigCount"
        us_rig_headers = {"Referer": self.us_rig_count}
        ca_rig_headers = {"Referer": self.ca_rig_count}
        yield Request(us_rig_request_url, method='GET', headers=us_rig_headers, callback=self.parse_us_rig)
        yield Request(ca_rig_request_url, method='GET', headers=ca_rig_headers, callback=self.parse_ca_rig)


    def parse_us_rig(self, response):
        data = json.loads(response.body.decode('utf-8'))[-5:]
        for i in data:
            date = datetime.datetime.strptime(i['Date'], '%Y-%m-%d')
            l = ItemLoader(item=Boe_US_rig_Item(), response=response)
            l.add_value('date', date)
            l.add_value('total', i['Total'])
            l.add_value('oil', i['Oil'])
            l.add_value('gas', i['Gas'])
            l.add_value('eagle_ford', i['Eagle Ford'])
            l.add_value('appalachian', i['Appalachian'])
            l.add_value('permian', i['Permian'])
            l.add_value('williston', i['Williston'])
            l.add_value('dj_niobrara', i['DJ-Niobrara'])
            l.add_value('other_basins', i['Other Basins'])
            yield l.load_item()


    def parse_ca_rig(self, response):
        data = json.loads(response.body.decode('utf-8'))[-5:]
        for i in data:
            date = datetime.datetime.strptime(i['Date'], '%Y-%m-%d')
            l = ItemLoader(item=Boe_CA_rig_Item(), response=response)
            l.add_value('date', date)
            l.add_value('total', i['Total'])
            l.add_value('gas', i['Gas'])
            l.add_value('oil', i['Oil'])
            l.add_value('alberta', i['Alberta'])
            l.add_value('bc', i['BC'])
            l.add_value('saskatchewan', i['Saskatchewan'])
            l.add_value('manitoba', i['Manitoba'])
            l.add_value('other_provinces', i['Other Provinces'])
            yield l.load_item()
