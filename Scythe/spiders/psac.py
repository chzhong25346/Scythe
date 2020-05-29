# -*- coding: utf-8 -*-
import scrapy
import datetime
from scrapy.http import Request
from scrapy.loader import ItemLoader
from Scythe.items import Psac_Item
from ..utils.utils import get_cell

class PsacSpider(scrapy.Spider):
    name = 'psac'
    allowed_domains = ['www.psac.ca']
    start_urls = ['https://www.psac.ca/business/marketstats/']

    def parse(self, response):
        # yield Request(self.start_urls[0], callback=self.parse_url)
        Request(self.start_urls[0])

    # def parse_url(self, response):
        date =  response.xpath('//td/strong/text()').re("^\d+\/\d+\/\d+$")[2]
        date = datetime.datetime.strptime(date, '%m/%d/%y')
        ex_rate = get_cell(response, "Can-US Exchange Rate (US ¢)", cell_num=0)/100
        aeco = round(get_cell(response, "Daily Spot AECO")*ex_rate,2)
        station2 = round(get_cell(response, "Station 2")*ex_rate,2)
        dawn = round(get_cell(response, "Dawn, ON")*ex_rate,2)
        henry_aeco_diff = get_cell(response, "Daily Spot Diff. (H. Hub-AECO)")
        henry = get_cell(response, "Daily Spot Henry Hub")
        wti = get_cell(response, "Daily Spot WTI @Cushing")
        wcs = get_cell(response, "WCS @Hardisty")
        wti_wcs_diff = get_cell(response, "Differential (WTI-WCS)")
        sp_500_energy = get_cell(response, "S&P 500 Energy Index", cell_num=0)
        amex_oil = get_cell(response, "AMEX Oil Index", cell_num=0)
        tsx_energy = get_cell(response, "S&P/TSX Capped Energy Index", cell_num=0)
        tsx_og_producers = get_cell(response, "S&P/TSX Oil & Gas Producers", cell_num=0)
        tsx_og_services = get_cell(response, "S&P/TSX Oil & Gas Services", cell_num=0)
        ca_us_ex_rate = get_cell(response, "Can-US Exchange Rate (US ¢)", cell_num=0)
        tenyr_cdn_gov_bond_yield = get_cell(response, "10Yr CDN gov't bond yield", cell_num=0)
        l = ItemLoader(item=Psac_Item(), response=response)
        l.add_value('date', date)
        l.add_value('aeco', str(aeco))
        l.add_value('station2', str(station2))
        l.add_value('dawn', str(dawn))
        l.add_value('henry_aeco_diff', str(henry_aeco_diff))
        l.add_value('henry', str(henry))
        l.add_value('wti', str(wti))
        l.add_value('wcs', str(wcs))
        l.add_value('wti_wcs_diff', str(wti_wcs_diff))
        l.add_value('sp_500_energy', str(sp_500_energy))
        l.add_value('amex_oil', str(amex_oil))
        l.add_value('tsx_energy', str(tsx_energy))
        l.add_value('tsx_og_producers', str(tsx_og_producers))
        l.add_value('tsx_og_services', str(tsx_og_services))
        l.add_value('ca_us_ex_rate', str(ca_us_ex_rate))
        l.add_value('tenyr_cdn_gov_bond_yield', str(tenyr_cdn_gov_bond_yield))
        return l.load_item()
