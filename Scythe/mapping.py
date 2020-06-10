# -*- coding: utf-8 -*-

from .models import Enmax_load, ShpgxLng_load, Psac, Boe_US_rig, Boe_CA_rig, CIBC_metals
# from .utils.utils import gen_id


def map_enmax_load(item):
    load = Enmax_load()
    # load.id = gen_id(item['tou'] + str(item['date']))
    load.date = item['date']
    load.load = item['load']
    return load


def map_shpgxLng_load(item):
    load = ShpgxLng_load()
    load.date = item['date']
    load.rmb_ton = item['rmb_ton']
    load.dollar_mmbtu = item['dollar_mmbtu']
    load.rmb_gj = item['rmb_gj']
    return load


def map_psac(item):
    load = Psac()
    load.date = item['date']
    load.aeco = item['aeco']
    load.station2 = item['station2']
    load.dawn = item['dawn']
    load.henry_aeco_diff = item['henry_aeco_diff']
    load.henry = item['henry']
    load.wti = item['wti']
    load.wcs = item['wcs']
    load.wti_wcs_diff = item['wti_wcs_diff']
    load.sp_500_energy = item['sp_500_energy']
    load.amex_oil = item['amex_oil']
    load.tsx_energy = item['tsx_energy']
    load.tsx_og_producers = item['tsx_og_producers']
    load.tsx_og_services = item['tsx_og_services']
    load.ca_us_ex_rate = item['ca_us_ex_rate']
    load.tenyr_cdn_gov_bond_yield = item['tenyr_cdn_gov_bond_yield']
    return load


def map_boe_us_rig(item):
    load = Boe_US_rig()
    load.date = item['date']
    load.total = item['total']
    load.oil = item['oil']
    load.gas = item['gas']
    load.eagle_ford = item['eagle_ford']
    load.appalachian = item['appalachian']
    load.permian = item['permian']
    load.williston = item['williston']
    load.dj_niobrara = item['dj_niobrara']
    load.other_basins = item['other_basins']
    return load


def map_boe_ca_rig(item):
    load = Boe_CA_rig()
    load.date = item['date']
    load.total = item['total']
    load.oil = item['oil']
    load.gas = item['gas']
    load.alberta = item['alberta']
    load.bc = item['bc']
    load.saskatchewan = item['saskatchewan']
    load.manitoba = item['manitoba']
    load.other_provinces = item['other_provinces']
    return load


def map_cibc_metals(item):
    load = CIBC_metals()
    load.date = item['date']
    load.gbar_1oz = item['gbar_1oz']
    load.gcoin_1oz = item['gcoin_1oz']
    load.sbar_100oz = item['sbar_100oz']
    load.scoin_1oz = item['scoin_1oz']
    return load
