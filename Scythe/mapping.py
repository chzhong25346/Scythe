# -*- coding: utf-8 -*-

from .models import Enmax_load, ShpgxLng_load
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
