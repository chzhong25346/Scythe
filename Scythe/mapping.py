# -*- coding: utf-8 -*-

from .models import Enmax_load, ShpgxLng_load, Psac
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
    load.aeco = item['aeco']
    load.station2 = item['station2']
    load.dawn = item['dawn']
    load.henry_aeco_diff = item['henry_aeco_diff']
    load.henry = item['henry']
    load.wti = item['wti']
    load.wcs = item['wcs']
    load.wti_wcs_diff = item['wti_wcs_diff']
    load.date = item['date']
    return load
