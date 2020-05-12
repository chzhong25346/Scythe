# -*- coding: utf-8 -*-
import scrapy
import datetime
import logging
from pytz import timezone
from scrapy.http import Request
from scrapy.loader import ItemLoader
from Scythe.items import Enmax_Item
from ..utils.utils import is_between, gen_id


class EnmaxSpider(scrapy.Spider):
    name = 'enmax'
    allowed_domains = ['www.enmax.com']
    start_urls = ['https://www.enmax.com/generation-wires/real-time-system-demand/']
    # logger = logging.getLogger(name)

    def parse(self, response):
        yield Request(self.start_urls[0], callback=self.parse_load)

    def parse_load(self, response):
        self.logger.info(' >>> Scraping ENMAX Load')
        load = response.xpath('//span[@id="spanCurrentLoad"]/text()').extract_first()
        # Calculate Calgary time
        tz = timezone('America/Denver')
        date = datetime.datetime.now(tz).strftime("%Y-%m-%d")
        time = datetime.datetime.now(tz).strftime("%H:%M")
        # tou = None
        # if is_between(time, ("7:00", "11:00")):
        #     tou = 'on-peak-am'
        # elif is_between(time, ("17:00", "19:00")):
        #     tou = 'on-peak-pm'
        # elif is_between(time, ("11:00", "17:00")):
        #     tou = 'mid-peak'
        # elif is_between(time, ("19:00", "7:00")):
        #     tou = 'off-peak'

        l = ItemLoader(item=Enmax_Item(), response=response)
        l.add_value('load', load)
        # l.add_value('tou', tou)
        l.add_value('date', date)
        # l.add_value('id', gen_id(tou+str(date)))
        # self.logger.info(l.load_item())
        return l.load_item()
